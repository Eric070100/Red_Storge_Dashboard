
from django.db import models

class Plantel(models.Model):
    id_plantel = models.IntegerField(primary_key=True)
    nombre_plantel = models.CharField(max_length=300)
    domicilio = models.CharField(max_length=200)
    numero_telefono = models.CharField(max_length=200)

class Grupo(models.Model):
    id_grupo = models.IntegerField(primary_key=True)
    grado = models.IntegerField()
    letra = models.CharField(max_length=1)
    id_palntel = models.ForeignKey("escuelas.Plantel", \
        verbose_name="plantel", on_delete=models.CASCADE)
