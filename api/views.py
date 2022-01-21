from datetime import datetime
from api.models import candidatos, votaciones, votos_empleados
from django.utils import timezone
from api.serializers import ApiVotoSerializer, CandidatoSerializer, VotacionSerializer, VotoEmpleadoSerializer, puestoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes

@api_view(['GET'])
def votacion_activa(request):
    now = timezone.now()
    votacion = votaciones.objects.filter(publicacion__lt=now,cierre__gt=now).count()
    if votacion > 0:
        return Response({"votacion":True})
    else:
        return Response({"votacion":False})
    
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def voto(request):
    if request.method == 'GET':
        votacion = votaciones.objects.last()
        mivoto = votos_empleados.objects.filter(id_votante=request.user.id,id_votacion=votacion.id).count()
        if mivoto > 0:
            return Response({"voto":True})
        else:
            list_candidatos = candidatos.objects.filter(id_votaciones=votacion.id)
            serializer = CandidatoSerializer(list_candidatos, many=True)
            return Response({"candidatos":serializer.data})
    if request.method == 'POST':
        votacion = votaciones.objects.last()
        mivoto = votos_empleados.objects.filter(id_votante=request.user.id,id_votacion=votacion.id).count()
        #votos_num = candidatos.objects.filter(id_votacion=votacion.id)
        if mivoto > 0:
            return Response({"voto":True})
        VotoEmpleadoData = VotoEmpleadoSerializer(data=request.data)
        if VotoEmpleadoData.is_valid():
            info = 0
            api_empleado_voto_serializer = VotoEmpleadoSerializer(data={'id_votante':request.user.id,'id_votacion':votacion.id})
            if api_empleado_voto_serializer.is_valid():
                api_empleado_voto_serializer.save
                
            for x in VotoEmpleadoData.validated_data['voto']:
                api_voto_serializer = ApiVotoSerializer(data={'id_candidato':x['id'],'id_votacion':votacion.id})
                if api_voto_serializer.is_valid():
                    api_voto_serializer.save()
                    info =  info + 1
            
            return Response({"voto":info})
        return Response({"voto":False,"message":"Datos incorrectos"})

    