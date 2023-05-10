from django.urls import path, include
from django.contrib import admin
from escuelas import views

urlpatterns = [
    path('lista_planteles', views.ListaPlanteles.as_view(), name='lista_planteles'),
    path('lista_grupos', views.ListaGrupos.as_view(), name='lista_grupos'),
    path('nuevo_grupo', views.NuevoGrupo.as_view(), name='nuevo_grupo'),
    path('nuevo_plantel', views.NuevoPlantel.as_view(), name='nuevo_plantel')
]
