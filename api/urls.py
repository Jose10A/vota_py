from django.urls import path
from api import views
urlpatterns = [

    path("",views.hello_world.as_view(),name="hellow"),

    #--front
    #invitacion
    #votar
    #resultados
    
    #--panel
    #crear votacion -candidatos -puestos 
    #editar votacion -candidatos -puestos 
    #eliminar -candidatos -puestos 
    
    
    ]