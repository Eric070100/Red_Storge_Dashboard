from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Estudiante, Encargo_plantel
from .forms import FormEstudiante, FormEP, UserForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class ListaEstudiantes(LoginRequiredMixin,ListView):
    model = Estudiante
    login_url ='login'

class ListaEncargados(LoginRequiredMixin,ListView):
    model = Encargo_plantel
    login_url ='login'

class NuevoEstudiante(LoginRequiredMixin,CreateView):
    model = Estudiante
    form_class = FormEstudiante
    # fields = '__all__'
    success_url = reverse_lazy('lista_estudiantes')
    extra_context = {'accion': 'Nueva'}
    login_url ='login'

class NuevoEP(LoginRequiredMixin,CreateView):
    model = Encargo_plantel
    form_class = FormEP
    # fields = '__all__'
    success_url = reverse_lazy('lista_encargados')
    extra_context = {'accion': 'Nueva'}
    login_url ='login'

class RegistroEncargado(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'registrar_encargado.html'
    form_class = UserForm
    success_message = '%(username)s se registró con éxito'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form = UserForm(self.request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # miapp.com
            # localhost:8000
            dominio = get_current_site(self.request)
            mensaje = render_to_string('confirmar_cuenta.html',
                {
                    'user':user,
                    'dominio':dominio,
                    'uid': urlsafe_base64_encode(force_bytes(user.id)),
                    'token': token_activacion.make_token(user)
                }
            )

            email = EmailMessage(
                'Activar cuenta ',
                mensaje,
                to=[user.email]
            )
            email.content_subtype = "html"
            email.send()
        else:
            return self.render_to_response(self.get_context_data(form=form))
        return super().form_valid(form)
    
class RegistrarUsuario(LoginRequiredMixin,ListView):
    model = User
    template_name = 'registrar_usuario.html'

class LoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    success_url = 'lista_preguntas'
    login_url ='login'