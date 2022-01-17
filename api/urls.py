from django.urls import path
from api import views
urlpatterns = [

    path("disponibilidad",views.votacion_activa,name="hellow"),
    path("",views.voto,name="emision"),

    #--front
    #invitacion
    #votar
    #resultados
    
    #--panel
    #crear votacion -candidatos -puestos 
    #editar votacion -candidatos -puestos 
    #eliminar -candidatos -puestos 
    
    
    ]