from django.db import models


# Create your models here.

class Responsable(models.Model):
    nombre = models.CharField(max_length=32)
    rol = models.CharField(max_length=64)


class Incidencia(models.Model):
    TIPO_CHOICES = (
        ('Req', 'Requerimiento'),
        ('Err', 'Error'),
        ('Tar', 'Tarea'),
        ('ST', 'Subtarea'),
    )
    padre = models.ManyToManyField('Incidencia', on_delete=models.DO_NOTHING, null=False)
    tipo = models.CharField(choices=TIPO_CHOICES, max_length=3, null=False)
    codigo = models.CharField(max_length=32, null=False, primary_key=True)
    cartel = models.ForeignKey('Cartel', on_delete=models.DO_NOTHING, null=False)
    horas_estimadas = models.FloatField(null=False)
    horas_trabajadas = models.FloatField(null=False)
    sprint_inicio = models.ForeignKey('Sprint', null=False)
    sprint_fin = models.ForeignKey('Sprint', null=True)
    reasignada = models.BooleanField(null=False, default=False)
    fecha_produccion = models.DateField(null=True)



class Asignado(models.Model):
    responsable = models.ManyToManyField('Responsable', on_delete=models.DO_NOTHING, null=False)
    incidencia = models.ManyToManyField('Incidencia', on_delete=models.DO_NOTHING, null=False)
    fecha = models.DateField(null=False, blank=False)


class Sprint(models.Model):
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_fin = models.DateField(null=False, blank=False)
    numero = models.IntegerField(null=False, primary_key=True)
    proyecto = models.CharField(max_length=64, null=False)


class Cartel(models.Model):
    numero = models.IntegerField(null=False)
    modificada = models.BooleanField(null=False, default=False)
    descripcion = models.CharField(max_length=256, null=False)
    horas_asignadas = models.FloatField(null=False)
    horas_disponibles = models.FloatField(null=False)
    padre = models.ManyToManyField('Cartel', on_delete=models.DO_NOTHING, null=False)


class Planificacion(models.Model):
    ESTADO_CHOICES = (
        ('1', 'Por hacer'),
        ('2', 'En proceso'),
        ('3', 'Desarrollado'),
        ('4', 'En pruebas'),
        ('5', 'Aprobado por PO'),
        ('6', 'Hecho'),
        ('7', 'Pagada'),
        ('8', 'Por pagar'),
    )
    sprint = models.ManyToManyField('Cartel', on_delete=models.DO_NOTHING, null=False)
    incidencia = models.ManyToManyField('Incidencia', on_delete=models.DO_NOTHING, null=False)
    fecha = models.DateField(null=False, blank=False)
    estado = models.CharField(choices=ESTADO_CHOICES, max_length=2, null=False)


class Observacion(models.Model):
    fecha = models.DateField(null=False, blank=False)
    descripcion = models.CharField(max_length=512)
    incidencia = models.ForeignKey('Incidencia', on_delete=models.DO_NOTHING, null=False)
