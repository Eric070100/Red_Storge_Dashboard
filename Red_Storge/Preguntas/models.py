from django.db import models

FASE = [
    ('', '-------------'),
    (1, 'Bosque'),
    (2, 'Laberinto'),
    (3, 'Recuperación')
]

MODULO = {
    ('', '-------------'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
}

class Pregunta(models.Model):
    id_pregunta = models.IntegerField(primary_key=True)
    planteamiento = models.CharField(max_length=200)
    modulo = models.IntegerField(choices=FASE)

class Opcion(models.Model):
    id_opcion = models.IntegerField(primary_key=True)
    id_pregunta = models.ForeignKey("Preguntas.Pregunta", verbose_name="pregunta", on_delete=models.CASCADE)
    inciso = models.CharField(max_length=1)
    descripcion = models.CharField(max_length=200)

class Contestacion(models.Model):
    id_contestacion = models.IntegerField(primary_key=True)
    id_estudiante = models.ForeignKey("usuarios.Estudiante", verbose_name="usuario", on_delete=models.DO_NOTHING)
    id_opcion = models.ForeignKey("Preguntas.Pregunta", verbose_name="opcion", on_delete=models.CASCADE)
    tiempo_segundos = models.IntegerField()
    numero_intento = models.IntegerField()


