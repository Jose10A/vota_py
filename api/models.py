from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.



class votaciones(models.Model):
    titulo = models.TextField()
    cierre = models.DateTimeField()
    inicio = models.DateTimeField()
    publicacion = models.DateTimeField()
    
class configuracion(models.Model):
    convocatoria = models.TextField()

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

class empleados(AbstractBaseUser, PermissionsMixin):
    nombres = models.TextField()
    apellidos = models.TextField()
    no_expediente = models.TextField()
    email = models.EmailField(max_length=255, unique=True,default="example@gmail.com")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombres', 'apellidos','no_expediente']

    def get_full_name(self):
        return self.nombres

    def get_short_name(self):
        return self.nombres
    
    def __str__(self):
        return self.email

class votos_empleados(models.Model):
    id_votante = models.ForeignKey(empleados,on_delete=CASCADE)
    id_votacion = models.ForeignKey(votaciones,on_delete=CASCADE)
    emision = models.DateTimeField(auto_now=True)

class puestos(models.Model):
    titulo = models.TextField()
    
class candidatos(models.Model):
    id_empleado = models.ForeignKey(empleados,on_delete=CASCADE)
    id_puesto = models.ForeignKey(puestos,on_delete=CASCADE)
    id_votaciones = models.ForeignKey(votaciones, related_name='candidatura',default=1,on_delete=models.CASCADE)
    media = models.TextField()
    
class votos(models.Model):
    id_candidato = models.ForeignKey(candidatos,on_delete=CASCADE)
    id_votacion = models.ForeignKey(votaciones,on_delete=CASCADE,default=1)

class votos_historicos(models.Model):
    id_candidato = models.ForeignKey(candidatos,on_delete=models.CASCADE)
    id_votacion = models.ForeignKey(votaciones,on_delete=CASCADE)
    monto = models.IntegerField()