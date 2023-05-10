from django.urls import path, include
from django.contrib import admin
from Preguntas import views

urlpatterns = [
    path('lista_preguntas', views.lista_preguntas, name='lista_preguntas'),
    path('nueva_pregunta', views.NuevaPregunta.as_view(), name='nueva_pregunta'),
    path('editar/<str:pk>', views.EditarPregunta.as_view(), name='editar_pregunta'),
    path('eliminar/<str:pk>', views.EliminarPregunta.as_view(), name='eliminar_pregunta'),
]
