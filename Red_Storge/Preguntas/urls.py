from django.urls import path, include
from django.contrib import admin
from Preguntas import views

urlpatterns = [
    path('lista_preguntas', views.lista_preguntas, name='lista_preguntas'),
    path('nueva_pregunta', views.NuevaPregunta.as_view(), name='nueva_pregunta'),
    path('editar/<str:pk>', views.EditarPregunta.as_view(), name='editar_pregunta'),
    path('eliminar/<str:pk>', views.EliminarPregunta.as_view(), name='eliminar_pregunta'),
    path('lista_opciones', views.lista_opciones, name='lista_opciones'),
    path('nueva_opcion', views.NuevaOpcion.as_view(), name='nueva_opcion'),
    path('editar/<str:pk>', views.EditarOpcion.as_view(), name='editar_opcion'),
    path('eliminar/<str:pk>', views.EliminarOpcion.as_view(), name='eliminar_opcion'),
    path('lista_contestaciones', views.lista_contestaciones, name='lista_contestaciones'),
    path('nueva_contestacion', views.NuevaContestacion.as_view(), name='nueva_contestacion'),
    path('editar/<str:pk>', views.EditarContestacion.as_view(), name='editar_contestacion'),
    path('eliminar/<str:pk>', views.EliminarContestacion.as_view(), name='eliminar_contestacion'),
]
