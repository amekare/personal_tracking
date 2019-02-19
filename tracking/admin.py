from django.contrib import admin
from tracking.models import Incidencia, Sprint, Responsable, Planificacion

# Register your models here.

admin.site.register(Incidencia)
admin.site.register(Sprint)
admin.site.register(Responsable)
admin.site.register(Planificacion)