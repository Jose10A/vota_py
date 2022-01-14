from django.db.models import fields
from rest_framework import serializers
from Djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from api.models import empleados, votaciones, puestos

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = empleados
        fields = [ 'nombres', 'apellidos', 'no_expediente']

class VotacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = votaciones
        fields = [ 'titulo', 'inicio','cierre', 'publicacion']
        
class puestos(serializers.ModelSerializer):
    class Meta:
        model = puestos
        fields = [ 'titulo']
        
class puestos(serializers.ModelSerializer):
    class Meta:
        model = puestos
        fields = ['idpuesto', 'media']
        
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'nombres', 'password', 'no_expediente']       
    