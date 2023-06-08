from django.shortcuts import render
from usuarios.models import Estudiante
from escuelas.models import Grupo
from .models import Pregunta, Opcion, Contestacion, FASE
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import FormPregunta, FormPreguntaEditar, FormOpcion, FormOpcionEditar, FormContestacion, FormContestacionEditar
from django.db.models import Count 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class Home(LoginRequiredMixin,TemplateView):
    estudiantes_grupo = Estudiante.objects.all().values('grupo').annotate(cuantos=Count('grupo'))
    grupos = Grupo.objects.all()
    datos = []
    for grupo in grupos:
        cuantos = 0
        for eg in estudiantes_grupo:
            if eg['grupo'] == grupo.id_grupo:
                cuantos = eg['cuantos']
                break
        datos.append({'letra': grupos, 'data': [cuantos]})
        
    extra_context = {'datos': datos}
    template_name = 'home.html'
    login_url ='login'


#Preguntas
@login_required(login_url='login')
def lista_preguntas(request):
    context={
        "preguntas":Pregunta.objects.all()
    }
    #return(request, "lista_preguntas.html", context)
    return render(request, "lista_preguntas.html", context)
    login_url ='login'

class NuevaPregunta(LoginRequiredMixin,CreateView):
    model = Pregunta
    form_class = FormPregunta
    #fields = '__all__'
    success_url = reverse_lazy('lista_preguntas')
    extra_context = {'accion': 'Nueva'}
    login_url ='login'

class EditarPregunta(UpdateView):
    model = Pregunta
    form_class = FormPreguntaEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_preguntas')
    
class EliminarPregunta(DeleteView):
    model = Pregunta
    success_url = reverse_lazy('lista_preguntas')

#Opcion
@login_required(login_url='login')
def lista_opciones(request):
    context={
        "opciones":Opcion.objects.all()
    }
    #return(request, "lista_opciones.html", context)
    return render(request, "lista_opciones.html", context)
    login_url ='login'

class NuevaOpcion(LoginRequiredMixin,CreateView):
    model = Opcion
    form_class = FormOpcion
    #fields = '__all__'
    success_url = reverse_lazy('lista_opciones')
    extra_context = {'accion': 'Nueva'}
    login_url ='login'

class EditarOpcion(UpdateView):
    model = Opcion
    form_class = FormOpcionEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_opciones')
    
class EliminarOpcion(DeleteView):
    model = Opcion
    success_url = reverse_lazy('lista_opciones')

#Contestacion
@login_required(login_url='login')
def lista_contestaciones(request):
    context = {
        "contestaciones": Contestacion.objects.all()
    }
    return render(request, "lista_contestaciones.html", context)
    

class NuevaContestacion(LoginRequiredMixin,CreateView):
    model = Contestacion
    form_class = FormContestacion
    #fields = '__all__'
    success_url = reverse_lazy('lista_contestaciones')
    extra_context = {'accion': 'Nueva'}
    login_url ='login'

class EditarContestacion(UpdateView):
    model = Contestacion
    form_class = FormContestacionEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_contestaciones')
    
class EliminarContestacion(DeleteView):
    model = Contestacion
    success_url = reverse_lazy('lista_contestaciones')