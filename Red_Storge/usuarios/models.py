from django.db import models
from django.contrib.auth.models import User

class Estudiante(models.Model):
    nombre = models.CharField(max_length=150)
    apellido_paterno = models.CharField(max_length=150)
    apellido_materno = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()
    usuario = models.OneToOneField(User, verbose_name="Usuario", on_delete=models.CASCADE)
    grupo = models.ForeignKey("escuelas.Grupo", verbose_name="grupo", on_delete=models.CASCADE)

class Encargo_plantel(models.Model):
    nombre = models.CharField(max_length=150)
    apellido_paterno = models.CharField(max_length=150)
    apellido_materno = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()
    usuario = models.OneToOneField(User, verbose_name="Usuario", on_delete=models.CASCADE)
    plantel = models.ForeignKey("escuelas.Plantel", \
        verbose_name="plantel", on_delete=models.CASCADE)


