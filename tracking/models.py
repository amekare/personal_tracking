from django.db import models

# Create your models here.

class Responsable:
    nombre = models.CharField(max_length=32)
    rol = models.CharField(max_length=64)

class Incidencia:
    pass

class Sprint:
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_fin = models.DateField(null=False, blank=False)
    numero = models.IntegerField(null=False)

class Cartel:
    numero = models.IntegerField(null=False)
    modificada = models.BooleanField(null=False, default=False)

