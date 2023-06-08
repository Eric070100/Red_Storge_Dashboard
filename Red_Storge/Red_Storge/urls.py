
from django.contrib import admin
from django.urls import path, include
from Preguntas.views import Home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('preguntas/', include('Preguntas.urls')),
    path('escuelas/', include('escuelas.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('', Home.as_view(), name='home'),
]

#from django.contrib import admin
#from django.urls import path, include
#from materias.views import Bienvenida


#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('programas/', include('unidades_academicas.urls_programas')),
#    path('materias/', include('materias.urls')),
#    path('', Bienvenida.as_view(), name='bienvenida'),
#    path('usuarios/', include('usuarios.urls')),
#]