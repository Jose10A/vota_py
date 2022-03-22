from api import serializers
from api.models import candidatos, empleados, puestos, votaciones, votos_empleados, votos
from rest_framework import status, viewsets
from django.utils import timezone
from api.serializers import ApiVotoSerializer, CandidatoPanelSerializer, CandidatoSerializer, EmpleadoSerializer, VotacionSerializer, VotoEmpleadoSerializer, puestoSerializer, UserCreateSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.permission import IsStaffPermission
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view,permission_classes
from excel_response import ExcelResponse


@api_view(['GET'])
def votacion_activa(request):
    now = timezone.now()
    votacion = votaciones.objects.filter(inicio__lt=now,cierre__gt=now).count()
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
    
    
    
 
    
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def voto(request):
    if request.method == 'GET':
        now = timezone.now()
        votacion_activa = votaciones.objects.filter(inicio__lt=now,cierre__gt=now).count()
        if votacion_activa:
            votacion = votaciones.objects.filter(inicio__lt=now,cierre__gt=now).last()
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
        return Response({"message":"No hay votaciones disponibles"})
        
    if request.method == 'POST':
        now = timezone.now()
        votacion_activa = votaciones.objects.filter(inicio__lt=now,cierre__gt=now).last()
        voto_usuario = votos_empleados.objects.filter(id_votante=request.user.id,id_votacion=votacion_activa.id).count()
        votosData =  ApiVotoSerializer(data=request.data,many=True)
        votosInfo = VotoEmpleadoSerializer(data={"id_votante":request.user.id,"id_votacion":votacion_activa.id})
        
        if votacion_activa.id and  voto_usuario == 0 and votosData.is_valid() and votosInfo.is_valid():
                votosData.save()
                votosInfo.save()
                return Response({"voto":True})
        return Response({"voto":False,"message":"Datos incorrectos"})


#panel de administracion


class PuestosViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Puestos.
    """
    queryset = puestos.objects.all()
    serializer_class = puestoSerializer
    permission_classes = [IsAuthenticated,IsStaffPermission]

class VotacionesViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing votaciones.
    """
    queryset = votaciones.objects.all()
    serializer_class = VotacionSerializer
    permission_classes = [IsAuthenticated,IsStaffPermission]
    
class CandidatosViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Candidaturas.
    """
    queryset = candidatos.objects.all()
    default_serializer_class = CandidatoPanelSerializer
    permission_classes = [IsAuthenticated,IsStaffPermission]
    
       # mapping serializer into the action
    serializer_classes = {
        'list': serializers.CandidatoSerializer,
        'retrieve': serializers.CandidatoSerializer

    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

User = get_user_model()
class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Usuarios.
    """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [IsAuthenticated,IsStaffPermission]
    
    
    
    
@api_view(['GET','POST'])
def admin_candidatura(request):
    if request.method == 'GET':
        info=[]
        data = candidatos.objects.all()
        for row in data:
            info.append({"id":row.id,"empleado":row.id_empleado.nombres,"puesto":row.id_puesto.titulo,"votacion":row.id_votaciones.titulo})
        return Response({"res":info})
    if request.method == 'POST':
        votosInfo = CandidatoSerializer(data={"id_empleado":request.id_empleado,"id_puesto":request.id_puesto})
        return Response({"votacion":True})
        
@api_view(['GET'])
def votacion_general_info(request):
    if request.method == 'GET':
        votacion_activa = votaciones.objects.last()
        votos_emitidos = votos_empleados.objects.filter(id_votacion=votacion_activa.id).count()
        votos_totales = empleados.objects.count()
        return Response({"votacion":votacion_activa.titulo,"votos_realizados":votos_emitidos,"votos_totales":votos_totales})

       
@api_view(['GET'])
def relacion_faltante(request):
    if request.method == 'GET':
        info=[]
        votacion_activa = votaciones.objects.last()
        votos_emitidos = votos_empleados.objects.filter(id_votacion=votacion_activa.id).values('id_votante')
        for row in votos_emitidos:
            info.append(row['id_votante'])
        votos_faltantes = empleados.objects.exclude(id__in=info).values("nombres","apellidos","no_expediente")

        return ExcelResponse(votos_faltantes,"votos faltantes")

        
        
        
        
  


       