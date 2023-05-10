
from django.contrib import admin
from django.urls import path, include
from usuarios import views

urlpatterns = [
    path('lista_estudiantes', views.ListaEstudiantes.as_view(), name='lista_estudiantes'),
    path('nuevo_estudiante', views.NuevoEstudiante.as_view(), name='nuevo_estudiante'),
    path('lista_encargados', views.ListaEncargados.as_view(), name='lista_encargados'),
    path('nuevo_encargado', views.NuevoEP.as_view(), name='nuevo_encargado')
]

