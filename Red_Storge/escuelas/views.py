from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Plantel, Grupo
from .forms import FormPlantel, FormGrupo
from django.urls import reverse_lazy
# Create your views here.
class ListaPlanteles(ListView):
    model = Plantel

class ListaGrupos(ListView):
    model = Grupo

class NuevoPlantel(CreateView):
    model = Plantel
    form_class = FormPlantel
    # fields = '__all__'
    success_url = reverse_lazy('lista_planteles')
    extra_context = {'accion': 'Nueva'}

class NuevoGrupo(CreateView):
    model = Grupo
    form_class = FormGrupo
    # fields = '__all__'
    success_url = reverse_lazy('lista_grupos')
    extra_context = {'accion': 'Nueva'}