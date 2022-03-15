from django.urls import path
from api import views

user_panel_list = views.UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
votacion_panel_list = views.VotacionesViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

votacion_panel_pk_list = views.VotacionesViewSet.as_view({
    'get': 'retrieve',
    'post': 'update', 
})
candidato_panel_list = views.CandidatosViewSet.as_view({
    'get': 'list',
    'post': 'create' 
})
candidato_panel_pk_list = views.CandidatosViewSet.as_view({
    'get': 'retrieve',
    'post': 'update', 
    'delete': 'destroy'
})
puesto_panel_list = views.PuestosViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
puesto_panel_pk_list = views.PuestosViewSet.as_view({
    'get': 'retrieve',
    'post': 'update', 
    'delete': 'destroy'
})





urlpatterns = [

    #--endpoints del cliente
    path("votaciones/disponibilidad",views.votacion_activa,name="convocatoria"),
    path("votaciones/",views.voto,name="candidatos_voto"),
   

    #--endpoints del panel
    path("admin/dashboard/",views.votacion_general_info,name="dashboard"),
    path("admin/votacion/",votacion_panel_list,name="votacion_list"),
    path("admin/votacion/<int:pk>",votacion_panel_pk_list,name="votacion_pk"),
    path("admin/user/",user_panel_list,name="usuario_list"),
    path("admin/candidato/<int:pk>",candidato_panel_pk_list,name="candidato_pk"),
    path("admin/candidato/",candidato_panel_list,name="candidato_"),
    path("admin/puesto/<int:pk>",puesto_panel_pk_list,name="puesto_pk"),
    path("admin/puesto/",puesto_panel_list,name="puesto_")
    
    
    ]