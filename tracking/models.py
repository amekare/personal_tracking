from django.contrib.auth.models import User
from django.db import models


class Contratista(models.Model):
    nombre = models.CharField(max_length=32)
    apellido1 = models.CharField(max_length=32)
    apellido2 = models.CharField(max_length=32)
    identificacion = models.CharField(max_length=128)
    email = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Contratista'
        verbose_name_plural = 'Contratistas'

    def __str__(self):
        return self.nombre + " " + self.apellido1 + " " + self.apellido2


class Proyecto(models.Model):
    codigo = models.CharField(max_length=32, null=False, blank=False)
    nombre = models.CharField(max_length=256, null=False, blank=False)
    descripcion = models.CharField(max_length=512, null=False)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return "" + self.codigo + "-" + self.nombre


class Contratacion(models.Model):
    TIPO_CHOICES = (
        ('1', 'Externa por horas'),
        ('2', 'Externa por productos'),
        ('3', 'Interna CI'),
    )

    ROL_CHOICES = (
        ('1', 'Desarrollador(a)'),
        ('2', 'Analista'),
        ('3', 'Consultor(a)'),
    )

    tipo = models.CharField(choices=TIPO_CHOICES, max_length=3, null=False, blank=False)
    rol = models.CharField(choices=ROL_CHOICES, max_length=3, null=False, blank=False)
    proyecto = models.ForeignKey('Proyecto', null=False, blank=False, on_delete=models.DO_NOTHING)
    contratista = models.ForeignKey('Contratista', null=False, blank=False, on_delete=models.DO_NOTHING)
    contrato = models.CharField(max_length=1024, null=True, blank=True)
    orden_compra = models.CharField(max_length=128, null=True, blank=True)
    horas_contratadas = models.FloatField(null=True)
    horas_consumidas = models.FloatField(null=False, default=0)
    presupuesto_adjudicado = models.FloatField(null=True)
    presupuesto_consumido = models.FloatField(null=True)
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_fin = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Contratación'
        verbose_name_plural = 'Contrataciones'

    def __str__(self):
        return self.orden_compra + " - " + str(self.contratista)


class BitacoraContratacion(models.Model):
    observacion = models.CharField(max_length=1024, null=False, blank=False)
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    contratacion = models.ForeignKey('Contratacion', null=False, blank=False, on_delete=models.DO_NOTHING)

    # cambiar esto
    usuario = models.CharField(max_length=1024, null=False, blank=False)

    def __str__(self):
        return "" + self.codigo + "-" + self.nombre


class Producto(models.Model):
    numero = models.FloatField(blank=False, null=False)
    descripcion = models.CharField(max_length=1024, null=False, blank=False)
    horas_estimadas = models.FloatField(null=False)
    horas_utilizadas = models.FloatField(null=False, default=0)
    contratacion = models.ForeignKey('Contratacion', null=False, blank=False, on_delete=models.DO_NOTHING)
    modificado = models.BooleanField(null=False, default=False)
    pagado = models.BooleanField(null=False, default=False)
    padre = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.contratacion.contrato + " " + str(self.numero) + ": " + self.descripcion


class BitacoraProducto(models.Model):
    observacion = models.CharField(max_length=1024, null=False, blank=False)
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    producto = models.ForeignKey('Producto', null=False, blank=False, on_delete=models.DO_NOTHING)

    # cambiar esto
    usuario = models.CharField(max_length=1024, null=False, blank=False)

    def __str__(self):
        return "" + self.codigo + "-" + self.nombre


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
    horas_por_pagar = models.FloatField(null=False, default=0)
    producto = models.ForeignKey('Producto', blank=False, null=False, on_delete=models.DO_NOTHING)
    sprint_inicio = models.ForeignKey('Sprint', on_delete=models.DO_NOTHING, null=False, related_name="sprint_inicio")
    sprint_fin = models.ForeignKey('Sprint', on_delete=models.DO_NOTHING, null=True, related_name="sprint_fin",
                                   blank=True)
    reasignada = models.BooleanField(null=True, default=False)

    class Meta:
        verbose_name = 'Incidencia'
        verbose_name_plural = 'Incidencias'

    def __str__(self):
        return self.codigo


class Factura(models.Model):
    numero = models.CharField(max_length=25, null=False)
    fecha = models.DateField(null=False, blank=False)
    monto = models.FloatField(null=False)
    contratacion = models.ForeignKey('Contratacion', on_delete=models.DO_NOTHING, null=False, blank=False)

    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'

    def __str__(self):
        return self.numero + " - " + self.contratacion


class DetalleFactura(models.Model):
    planificacion = models.ForeignKey('Planificacion', on_delete=models.DO_NOTHING, null=False, blank=False)
    horas_facturadas = models.FloatField(null=True, default=0)
    monto_facturado = models.FloatField(null=False)
    factura = models.ForeignKey('Factura', on_delete=models.DO_NOTHING, null=False, blank=False)

    class Meta:
        verbose_name = 'Detalle de factura'
        verbose_name_plural = 'Detalles de factura'

    def __str__(self):
        return self.factura + " " + self.planificacion

class Sprint(models.Model):
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_fin = models.DateField(null=False, blank=False)
    fecha_revision = models.DateField(null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    proyecto = models.ForeignKey('Proyecto', null=False, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ["numero", "proyecto"]
        unique_together = ('numero', 'proyecto')
        verbose_name = 'Sprint'
        verbose_name_plural = 'Sprints'

    def __str__(self):
        return "Sprint " + self.numero.__str__() + "-" + self.proyecto




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
    CLASIFICACION_CHOICES = (
        ('1', 'Sin pagar'),
        ('2', 'Por pagar'),
        ('3', 'Pagada'),
        ('4', 'Desarrollo CI'),
        ('5', 'Garantía'),
    )
    estado_inicio = models.CharField(choices=ESTADO_CHOICES, max_length=2, null=False, blank=False)
    estado_fin = models.CharField(choices=ESTADO_CHOICES, max_length=2, null=True, blank=True)
    sprint = models.ForeignKey('Sprint', on_delete=models.DO_NOTHING, null=False, blank=False)
    incidencia = models.ForeignKey('Incidencia', on_delete=models.DO_NOTHING, null=False, blank=False)
    fecha_asignada = models.DateField(null=False, blank=False, auto_now_add=True)
    contratacion = models.ForeignKey('Contratacion', on_delete=models.DO_NOTHING, null=False, blank=False)
    clasificacion = models.CharField(choices=CLASIFICACION_CHOICES, max_length=3, null=False, blank=False, default='1')
    facturacion = models.BooleanField(null=False, default=False)

    class Meta:
        ordering = ["sprint", "fecha_asignada"]
        verbose_name = "Planificación"
        verbose_name_plural = "Planificaciones"

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




class Observacion(models.Model):
    fecha = models.DateField(null=False, blank=False, auto_now_add=True)
    descripcion = models.CharField(max_length=512)
    planificacion = models.ForeignKey('Planificacion', on_delete=models.DO_NOTHING, null=False)

    class Meta:
        ordering = ["fecha"]
        verbose_name = "Observación"
        verbose_name_plural = "Observaciones"

    def __str__(self):
        return self.fecha.__str__() + " " + self.planificacion.__str__()

