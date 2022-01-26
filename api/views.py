from datetime import datetime
from api.models import candidatos, votaciones, votos_empleados, votos
from django.utils import timezone
from api.serializers import ApiVotoSerializer, CandidatoSerializer, VotacionSerializer, VotoEmpleadoSerializer, puestoSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from api.permission import IsStaffPermission
from rest_framework.decorators import api_view,permission_classes

@api_view(['GET'])
def votacion_activa(request):
    now = timezone.now()
    votacion = votaciones.objects.filter(publicacion__lt=now,cierre__gt=now).count()
    if votacion > 0:
        return Response({"votacion":True})
    else:
        return Response({"votacion":False})

@api_view(['GET'])
def votacion_activa_reporte(request):
    now = timezone.now()
    votacion_cerrada = votaciones.objects.filter(cierre__lt=now).last()
    votos_reporte = votos.objects.filter(id_votacion=votacion_activa.id)
    votos_data    = ApiVotoSerializer(votos_reporte.data)
    info= {}
    for obj in votos_data:
        if  info.get(obj.id_candidato)!= None:
             info[obj.id_candidato].append(obj)
        else:
            info[obj.id_candidato] = [obj]
    return Response({"candidatos":info})
    
    
    
    
    if votacion_cerrada.id:
        return Response({"votacion":True})
    else:
        return Response({"resultados":False})
    
    
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def voto(request):
    if request.method == 'GET':
        now = timezone.now()
        votacion = votaciones.objects.filter(publicacion__lt=now,cierre__gt=now).last()
        mivoto = votos_empleados.objects.filter(id_votante=request.user.id,id_votacion=votacion.id).count()
        if mivoto > 0:
            return Response({"voto":True})
        else:
            l_can_grouped = {}
            l_can= candidatos.objects.filter(id_votaciones=votacion.id)
            for obj in l_can:
                serializer = CandidatoSerializer(obj)
                if  l_can_grouped.get(obj.id_puesto.id)!= None :
                    l_can_grouped[obj.id_puesto.id].append(serializer.data)
                else:
                    l_can_grouped[obj.id_puesto.id] = [serializer.data]
            return Response({"candidatos":l_can_grouped})
        
    if request.method == 'POST':
        now = timezone.now()
        votacion_activa = votaciones.objects.filter(publicacion__lt=now,cierre__gt=now).last()
        voto_usuario = votos_empleados.objects.filter(id_votante=request.user.id,id_votacion=votacion_activa.id).count()
        votosData =  ApiVotoSerializer(data=request.data,many=True)
        votosInfo = VotoEmpleadoSerializer(data={"id_votante":request.user.id,"id_votacion":votacion_activa.id})
        if votacion_activa.id and  voto_usuario == 0 and votosData.is_valid() and votosInfo.is_valid():
                votosData.save()
                votosInfo.save()
                return Response({"voto":True})
        return Response({"voto":False,"message":"Datos incorrectos","valores":[]})


#panel de administracion
@api_view(['GET'])
@permission_classes([IsAuthenticated,IsStaffPermission])
def votacion_general_info():
    now = timezone.now()
    votacion = votaciones.objects.filter(publicacion__lt=now,cierre__gt=now).last()
    voto_emp = votos_empleados.objects.filter(id_votacion=votacion.id).count()
    num_emp = votos_empleados.objects.all().count()
    return Response({"votos":voto_emp,"numero_empleados":num_emp})