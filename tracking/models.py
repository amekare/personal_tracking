from django.contrib.auth.models import User
from django.db import models


class Contratista(models.Model):
    nombre = models.CharField(max_length=32)
    identificacion = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre


class Proyecto(models.Model):
    nombre = models.CharField(max_length=256, null=False, blank=False)
    descripcion = models.CharField(max_length=512, null=False)
    codigo = models.CharField(max_length=32, null=False, blank=False)

    def __str__(self):
        return "" + self.codigo + "-" + self.nombre


class Contratacion(models.Model):
    TIPO_CHOICES = (
        ('1', 'Externa'),
        ('2', 'Interna'),
    )

    ROL_CHOICES = (
        ('1', 'Desarrollador(a)'),
        ('2', 'Analista'),
        ('3', 'Consultor(a)'),
    )

    tipo = models.CharField(choices=TIPO_CHOICES, max_length=3, null=False, blank=False)
    rol = models.CharField(choices=ROL_CHOICES, max_length=3, null=False, blank=False)
    contratista = models.ForeignKey('Contratista', null=False, blank=False, on_delete=models.DO_NOTHING)
    proyecto = models.ForeignKey('Proyecto', null=False, blank=False, on_delete=models.DO_NOTHING)
    contrato = models.CharField(max_length=1024, null=False, blank=False)
    orden_compra = models.CharField(max_length=128, null=False, blank=False)
    horas_contratadas = models.FloatField(null=False)
    horas_consumidas = models.FloatField(null=False)
    presupuesto_asignado = models.FloatField(null=False)
    presupuesto_consumido = models.FloatField(null=False)
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_fin = models.DateField(null=True, blank=True)
    vigencia_dias = models.IntegerField(null=False, blank=False)
    pago_hora = models.FloatField(null=False, blank=False)


class Bitacora_contratacion(models.Model):
    observacion = models.CharField(max_length=1024, null=False, blank=False)
    fecha = models.DateTimeField(auto_now=True, auto_now_add=True, blank=True)
    # cambiar esto
    usuario = models.ForeignKey('auth.User')
    contratacion = models.ForeignKey('Contratacion', null=False, blank=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "" + self.codigo + "-" + self.nombre


class Producto(models.Model):
    numero = models.FloatField(blank=False, null=False)
    descripcion = models.CharField(max_length=1024, null=False, blank=False)
    horas_estimadas = models.FloatField(null=False)
    contratacion = models.ForeignKey('Contratacion', null=False, blank=False, on_delete=models.DO_NOTHING)
    modificada = models.BooleanField(null=False, default=False)
    padre = models.ForeignKey('Cartel', on_delete=models.DO_NOTHING, null=True, blank=True)


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
        ('7', 'Pagada'),
        ('8', 'Por pagar'),
    )
    codigo = models.CharField(max_length=32, unique=True)
    descripcion = models.CharField(max_length=256, null=False)
    estado = models.CharField(choices=ESTADO_CHOICES, max_length=2, null=False)
    tipo = models.CharField(choices=TIPO_CHOICES, max_length=3, null=False)
    padre = models.ForeignKey('self', null=True, blank=True, on_delete=models.DO_NOTHING)
    horas_estimadas = models.FloatField(null=False, default=0)
    horas_trabajadas = models.FloatField(null=False, default=0)
    producto = models.ForeignKey('Producto', blank=False, null=False, on_delete=models.DO_NOTHING)
    sprint_inicio = models.ForeignKey('Sprint', on_delete=models.DO_NOTHING, null=False, related_name="sprint_inicio")
    sprint_fin = models.ForeignKey('Sprint', on_delete=models.DO_NOTHING, null=True, related_name="sprint_fin",
                                   blank=True)
    reasignada = models.BooleanField(null=False, default=False)
    fecha_produccion = models.DateField(null=True, blank=True)
    estado = models.CharField(choices=ESTADO_CHOICES, max_length=2, null=False)

    def __str__(self):
        return self.codigo


class Asignacion(models.Model):
    CLASIFICACION_CHOICES = (
        ('1', 'Sin pagar'),
        ('2', 'Por pagar'),
        ('3', 'Pagada'),
        ('4', 'Desarrollo CI'),
        ('5', 'Garantía'),
    )
    planificacion = models.ForeignKey('Planificacion', on_delete=models.DO_NOTHING, null=False, blank=False)
    contratacion = models.ForeignKey('Contratacion', on_delete=models.DO_NOTHING, null=False, blank=False)
    clasificacion = models.CharField(choices=CLASIFICACION_CHOICES, max_length=3, null=False, blank=False)
    facturacion = models.BooleanField(null=False, default=False)
    horas_facturadas = models.FloatField(null=False)
    monto_facturado = models.FloatField(null=False)


# cambiar
class Facturacion(models.Model):
    asignacion = models.ForeignKey('Asignacion', on_delete=models.DO_NOTHING, null=False, blank=False)


class Sprint(models.Model):
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_fin = models.DateField(null=False, blank=False)
    fecha_revision = models.DateField(null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    proyecto = models.ForeignKey('Proyecto', null=False)

    def __str__(self):
        return "Sprint " + self.numero.__str__() + "-" + self.proyecto

    class Meta:
        ordering = ["numero", "proyecto"]
        unique_together = ('numero', 'proyecto')



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
        ('9', 'En espera'),
    )
    estado_inicio = models.CharField(choices=ESTADO_CHOICES, max_length=2, null=False)
    estado_fin = models.CharField(choices=ESTADO_CHOICES, max_length=2, null=False, blank=True)
    sprint = models.ForeignKey('Sprint', on_delete=models.DO_NOTHING, null=False, blank=False)
    incidencia = models.ForeignKey('Incidencia', on_delete=models.DO_NOTHING, null=False, blank=False)
    fecha_asignada = models.DateField(null=False, blank=False, auto_now_add=True)

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
    fecha = models.DateField(null=False, blank=False, auto_now_add=True)
    descripcion = models.CharField(max_length=512)
    planificacion = models.ForeignKey('Planificacion', on_delete=models.DO_NOTHING, null=False)

    def __str__(self):
        return self.fecha.__str__() + " " + self.planificacion.__str__()

    class Meta:
        ordering = ["fecha"]
