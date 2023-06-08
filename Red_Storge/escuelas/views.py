from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Plantel, Grupo
from .forms import FormPlantel, FormGrupo,  FormGrupoEditar, FormPlantelEditar
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class ListaPlanteles(LoginRequiredMixin,ListView):
    model = Plantel
    login_url ='login'

class ListaGrupos(LoginRequiredMixin,ListView):
    model = Grupo
    login_url ='login'

class NuevoPlantel(LoginRequiredMixin,CreateView):
    model = Plantel
    form_class = FormPlantel
    # fields = '__all__'
    success_url = reverse_lazy('lista_planteles')
    extra_context = {'accion': 'Nueva'}
    login_url ='login'

class NuevoGrupo(LoginRequiredMixin,CreateView):
    model = Grupo
    form_class = FormGrupo
    # fields = '__all__'
    success_url = reverse_lazy('lista_grupos')
    extra_context = {'accion': 'Nueva'}
    login_url ='login'

class EditarGrupo(UpdateView):
    model = Grupo
    form_class = FormGrupoEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_grupos')
    
class EliminarGrupo(DeleteView):
    model = Grupo
    success_url = reverse_lazy('lista_grupos')

class EditarPlantel(UpdateView):
    model = Plantel
    form_class = FormPlantelEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_planteles')
    
class EliminarPlantel(DeleteView):
    model = Plantel
    success_url = reverse_lazy('lista_plantales')