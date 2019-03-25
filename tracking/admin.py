from django.contrib import admin
from tracking.models import Incidencia, Sprint, Responsable, Planificacion, Cartel, Observacion


class ResponsableAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rol')
    search_fields = ('nombre', 'rol')
    ordering = ('nombre',)


class IncidenciaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'codigo', 'descripcion', 'cartel', 'estado')
    search_fields = ('tipo', 'codigo', 'estado')
    list_filter = ('estado', 'tipo')
    ordering = ('codigo',)


class SprintAdmin(admin.ModelAdmin):
    list_display = ('numero', 'proyecto', 'fecha_inicio', 'fecha_fin')
    search_fields = ('numero', 'proyecto')
    ordering = ('numero', 'proyecto')


class CartelAdmin(admin.ModelAdmin):
    list_display = ('numero', 'descripcion', 'horas_asignadas', 'horas_disponibles')
    search_fields = ('numero', 'descripcion')
    ordering = ("numero",)


class PlanificacionAdmin(admin.ModelAdmin):
    list_display = ('sprint', 'incidencia', 'asignado', 'estado_inicio', 'estado_fin', 'pago')
    search_fields = ('sprint__numero', 'sprint__proyecto', 'incidencia__codigo', 'asignado__nombre')
    ordering = ("sprint",)
    list_filter = ("pago", "sprint", "asignado")


class ObservacionAdmin(admin.ModelAdmin):
    list_display = ('planificacion', 'descripcion', 'fecha')
    search_fields = ('planificacion',)
    ordering = ("fecha",)


admin.site.register(Incidencia, IncidenciaAdmin)
admin.site.register(Sprint, SprintAdmin)
admin.site.register(Responsable, ResponsableAdmin)
admin.site.register(Planificacion, PlanificacionAdmin)
admin.site.register(Cartel, CartelAdmin)
admin.site.register(Observacion, ObservacionAdmin)
