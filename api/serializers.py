from msilib.schema import Class
from django.db.models import fields
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from api.models import empleados, votaciones, puestos, candidatos

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = empleados
        fields = [ 'nombres', 'apellidos', 'no_expediente']

class VotacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = votaciones
        fields = [ 'titulo', 'inicio','cierre', 'publicacion']
        
class puestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = puestos
        fields = [ 'id','titulo']
        
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'nombres', 'password', 'no_expediente']     

class UserShowSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [ 'nombres','apellidos']


        
class CandidatoSerializer(serializers.ModelSerializer):
    id_puesto = puestoSerializer()
    id_empleado = UserShowSerializer()
    class Meta:
        model = candidatos
        fields = "__all__"
        ordering = ['id_puesto']

        

    