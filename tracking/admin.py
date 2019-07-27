from django.contrib import admin
from tracking.models import Incidencia, Sprint, Contratista, Planificacion, Producto, Observacion, Contratacion


class ContratistaAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'nombre', 'apellido1', 'apellido2')
    search_fields = ('nombre', 'apellido1', 'apellido2')
    ordering = ('nombre',)


class IncidenciaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'codigo', 'descripcion', 'producto', 'estado')
    search_fields = ('tipo', 'codigo', 'estado')
    list_filter = ('estado', 'tipo')
    ordering = ('codigo',)


class SprintAdmin(admin.ModelAdmin):
    list_display = ('numero', 'proyecto', 'fecha_inicio', 'fecha_fin')
    search_fields = ('numero', 'proyecto')
    ordering = ('numero', 'proyecto')


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'descripcion', 'horas_estimadas', 'horas_utilizadas')
    search_fields = ('numero', 'descripcion')
    ordering = ("numero",)


class PlanificacionAdmin(admin.ModelAdmin):
    list_display = (
        'sprint', 'incidencia', 'estado_inicio', 'estado_fin')
    search_fields = ('sprint__numero', 'sprint__proyecto', 'incidencia__codigo')
    ordering = ("sprint",)
    list_filter = ("sprint",)


class ObservacionAdmin(admin.ModelAdmin):
    list_display = ('planificacion', 'descripcion', 'fecha')
    search_fields = ('planificacion',)
    ordering = ("fecha",)


class ContratacionAdmin(admin.ModelAdmin):
    list_display = ('contratista', 'tipo', 'rol', 'proyecto', 'orden_compra',)
    search_fields = ('proyecto__codigo', 'proyecto__nombre', 'contratista__nombre')
    ordering = ("contratista", "proyecto")


admin.site.register(Incidencia, IncidenciaAdmin)
admin.site.register(Sprint, SprintAdmin)
admin.site.register(Contratista, ContratistaAdmin)
admin.site.register(Planificacion, PlanificacionAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Observacion, ObservacionAdmin)
admin.site.register(Contratacion, ContratacionAdmin)
