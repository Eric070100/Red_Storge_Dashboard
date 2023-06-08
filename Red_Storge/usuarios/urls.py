from django.contrib import admin
from django.urls import path
from usuarios import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('lista_estudiantes/', views.ListaEstudiantes.as_view(), name='lista_estudiantes'),
    path('nuevo_estudiante/', views.NuevoEstudiante.as_view(), name='nuevo_estudiante'),
    path('lista_encargados/', views.ListaEncargados.as_view(), name='lista_encargados'),
    path('nuevo_encargado/', views.NuevoEP.as_view(), name='nuevo_encargado'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('signin/', views.RegistrarUsuario.as_view(), name='signin'),
]
