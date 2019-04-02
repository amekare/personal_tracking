from django.db import models


# Create your models here.

class Responsable(models.Model):
    nombre = models.CharField(max_length=32)
    rol = models.CharField(max_length=64)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]


class Incidencia(models.Model):
    TIPO_CHOICES = (
        ('Req', 'Requerimiento'),
        ('Err', 'Error'),
        ('Tar', 'Tarea'),
        ('Sub', 'Subtarea'),
        ('Epi', 'Epic'),
    )
    ESTADO_CHOICES = (
        ('1', 'Por hacer'),
        ('2', 'En proceso'),
        ('3', 'Desarrollado'),
        ('4', 'En pruebas'),
        ('5', 'Aprobado por PO'),
        ('6', 'Hecho'),
        ('7', 'Cancelada'),

    )
    padre = models.ForeignKey('self', null=True, blank=True, on_delete=models.DO_NOTHING)
    tipo = models.CharField(choices=TIPO_CHOICES, max_length=3, null=False)
    descripcion = models.CharField(max_length=256, null=False)
    codigo = models.CharField(max_length=32, unique=True)
    cartel = models.ForeignKey('Cartel', on_delete=models.DO_NOTHING, null=False)
    horas_estimadas = models.FloatField(null=False)
    horas_trabajadas = models.FloatField(null=False)
    sprint_inicio = models.ForeignKey('Sprint', on_delete=models.DO_NOTHING, null=False, related_name="sprint_inicio")
    sprint_fin = models.ForeignKey('Sprint', on_delete=models.DO_NOTHING, null=True, related_name="sprint_fin",
                                   blank=True)
    reasignada = models.BooleanField(null=False, default=False)
    fecha_produccion = models.DateField(null=True, blank=True)
    estado = models.CharField(choices=ESTADO_CHOICES, max_length=2, null=False)

    def __str__(self):
        return self.codigo

    class Meta:
        ordering = ["codigo"]


class Sprint(models.Model):
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_fin = models.DateField(null=False, blank=False)
    fecha_revision = models.DateField(null=False, blank=False)
    numero = models.IntegerField(null=False)
    proyecto = models.CharField(max_length=64, null=False)

    def __str__(self):
        return "Sprint " + self.numero.__str__() + "-" + self.proyecto

    class Meta:
        ordering = ["numero", "proyecto"]
        unique_together = ('numero', 'proyecto')


class Cartel(models.Model):
    numero = models.FloatField(null=False)
    modificada = models.BooleanField(null=False, default=False)
    descripcion = models.CharField(max_length=256, null=False)
    horas_asignadas = models.FloatField(null=False)
    horas_disponibles = models.FloatField(null=False)
    padre = models.ForeignKey('Cartel', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.numero.__str__()

    class Meta:
        ordering = ["numero"]


class Planificacion(models.Model):
    ESTADO_CHOICES = (
        ('1', 'Por hacer'),
        ('2', 'En proceso'),
        ('3', 'Desarrollado'),
        ('4', 'En pruebas'),
        ('5', 'Aprobado por PO'),
        ('6', 'Hecho'),
        ('7', 'Cancelada'),
    )
    PAGO_CHOICES = (
        ('1', 'Pagada'),
        ('2', 'Por pagar'),
        ('3', 'Sin completar'),
        ('4', 'Desarrollo CI'),
        ('5', 'Errores'),
    )
    estado_inicio = models.CharField(choices=ESTADO_CHOICES, max_length=2, null=True, blank=True)
    estado_fin = models.CharField(choices=ESTADO_CHOICES, max_length=2, null=True, blank=True)
    sprint = models.ForeignKey('Sprint', on_delete=models.DO_NOTHING, null=False, blank=False)
    incidencia = models.ForeignKey('Incidencia', on_delete=models.DO_NOTHING, null=False, blank=False)
    fecha = models.DateField(null=False, blank=False)
    asignado = models.ForeignKey('Responsable', on_delete=models.DO_NOTHING, null=False, blank=False)
    pago = models.CharField(choices=PAGO_CHOICES, max_length=2, null=False, blank=False, default='3')

    def horas_estimadas(self):
        return self.incidencia.horas_estimadas

    def horas_trabajadas(self):
        return self.incidencia.horas_trabajadas

    def __str__(self):
        return self.sprint.__str__() + "(" + self.fecha.__str__() + ") -" + self.incidencia.codigo

    def save(self, *args, **kwargs):
        if not self.estado_inicio:
            self.estado_inicio = self.incidencia.estado
        if self.estado_fin:
            self.incidencia.estado = self.estado_fin
            if self.estado_fin == "6":
                self.incidencia.sprint_fin = self.sprint
            self.incidencia.save()

        super(Planificacion, self).save(*args, **kwargs)

    def get_sprint(self, obj):
        return obj.sprint

    class Meta:
        ordering = ["sprint", "fecha"]


class Observacion(models.Model):
    fecha = models.DateField(null=False, blank=False)
    descripcion = models.CharField(max_length=512)
    planificacion = models.ForeignKey('Planificacion', on_delete=models.DO_NOTHING, null=False)

    def __str__(self):
        return self.fecha.__str__() + " " + self.planificacion.__str__()

    class Meta:
        ordering = ["fecha"]
