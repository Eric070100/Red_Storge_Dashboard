from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Estudiante, Encargo_plantel
from .forms import FormEstudiante, FormEP
from django.urls import reverse_lazy

# Create your views here.
class ListaEstudiantes(ListView):
    model = Estudiante

class ListaEncargados(ListView):
    model = Encargo_plantel

class NuevoEstudiante(CreateView):
    model = Estudiante
    form_class = FormEstudiante
    # fields = '__all__'
    success_url = reverse_lazy('lista_estudiantes')
    extra_context = {'accion': 'Nueva'}

class NuevoEP(CreateView):
    model = Encargo_plantel
    form_class = FormEP
    # fields = '__all__'
    success_url = reverse_lazy('lista_encargados')
    extra_context = {'accion': 'Nueva'}