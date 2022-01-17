from datetime import datetime
from api.models import candidatos, votaciones, votos_empleados
from django.utils import timezone
from api.serializers import CandidatoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

@api_view(['GET'])
def votacion_activa(request):
    now = timezone.now()
    votacion = votaciones.objects.filter(publicacion__lt=now).count()
    if votacion > 0:
        return Response({"message": True})
    else:
        return Response({"votacion":False})
    
@api_view(['GET'])
def voto(request):
    mivoto = votos_empleados.objects.filter(id_votante=2).count()
    if mivoto > 0:
        return Response({"message": "ya votaste perro"})
    else:
        votacion = votaciones.objects.last()
        list_candidatos = candidatos.objects.filter(id_votaciones=votacion.id)
        serializer = CandidatoSerializer(list_candidatos, many=True)
        return Response({"data":serializer.data})
    