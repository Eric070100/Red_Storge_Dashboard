from django.shortcuts import render
from .models import Pregunta
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import FormPregunta, FormPreguntaEditar

class Home(TemplateView):
    template_name = 'home.html'

def lista_preguntas(request):
    context={
        "preguntas":Pregunta.objects.all()
    }
    #return(request, "lista_preguntas.html", context)
    return render(request, "lista_preguntas.html", context)

class NuevaPregunta(CreateView):
    model = Pregunta
    form_class = FormPregunta
    #fields = '__all__'
    success_url = reverse_lazy('lista_preguntas')
    extra_context = {'accion': 'Nueva'}

class EditarPregunta(UpdateView):
    model = Pregunta
    form_class = FormPreguntaEditar
    extra_context = {'accion': 'Editar'}
    success_url = reverse_lazy('lista_preguntas')
    
class EliminarPregunta(DeleteView):
    model = Pregunta
    success_url = reverse_lazy('lista_preguntas')



