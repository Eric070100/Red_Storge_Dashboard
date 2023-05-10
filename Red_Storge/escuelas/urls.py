from django.urls import path, include
from django.contrib import admin
from escuelas import views

urlpatterns = [
    path('lista_planteles', views.ListaPlanteles.as_view(), name='lista_planteles'),
    path('lista_grupos', views.ListaGrupos.as_view(), name='lista_grupos'),
    path('nuevo_grupo', views.NuevoGrupo.as_view(), name='nuevo_grupo'),
    path('nuevo_plantel', views.NuevoPlantel.as_view(), name='nuevo_plantel'),
    path('editar/<str:pk>', views.EditarGrupo.as_view(), name='editar_grupo'),
    path('eliminar/<str:pk>', views.EliminarGrupo.as_view(), name='eliminar_grupo'),
    path('editar/<str:pk>', views.EditarGrupo.as_view(), name='editar_plantel'),
    path('eliminar/<str:pk>', views.EliminarGrupo.as_view(), name='eliminar_plantel'),
]
