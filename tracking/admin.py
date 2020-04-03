from django.contrib import admin
from tracking.models import Incidencia, Sprint, Contratista, Planificacion, Producto, Observacion, Contratacion, \
    Proyecto


class ContratistaAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'nombre', 'apellido1', 'apellido2', 'email')
    search_fields = ('nombre', 'apellido1', 'apellido2')
    ordering = ('nombre',)


class IncidenciaAdmin(admin.ModelAdmin):
    list_display = (
        'codigo', 'tipo', 'descripcion', 'producto', 'estado', 'horas_estimadas', 'horas_trabajadas', 'clasificacion')
    search_fields = ('tipo', 'codigo', 'estado', 'descripcion')
    list_filter = ('estado', 'tipo', 'clasificacion')
    ordering = ('numero',)


class SprintAdmin(admin.ModelAdmin):
    list_display = ('numero', 'proyecto', 'fecha_inicio', 'fecha_fin')
    search_fields = ('numero', 'proyecto')
    ordering = ('numero', 'proyecto')
    list_filter = ("proyecto__nombre",)


class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'numero', 'descripcion', 'horas_estimadas', 'horas_utilizadas', 'horas_pagadas', 'modificado', 'pagado')
    search_fields = ('numero', 'descripcion')
    ordering = ("numero",)
    list_filter = ("contratacion__contrato", "contratacion__proyecto__nombre")


class PlanificacionAdmin(admin.ModelAdmin):
    list_display = ('sprint',
                    'incidencia', 'estado_inicio', 'estado_fin', 'contratista')
    search_fields = ('estado_inicio', "incidencia__codigo", "sprint__proyecto__nombre")
    ordering = ("sprint__proyecto", "sprint__numero", "incidencia__codigo")
    list_filter = ("sprint__proyecto",)

    def proyecto(self, obj):
        return obj.sprint.proyecto

    def contratista(self, obj):
        return obj.contratacion.contratista


class ObservacionAdmin(admin.ModelAdmin):
    list_display = ('sprint', 'incidencia', 'descripcion', 'fecha')
    search_fields = ('planificacion',)
    ordering = ("fecha",)

    def sprint(self, obj):
        return obj.planificacion.sprint.__str__() + " (" + str(obj.planificacion.sprint.fecha_inicio) + ")"

    def incidencia(self, obj):
        return obj.planificacion.incidencia


class ContratacionAdmin(admin.ModelAdmin):
    list_display = ('contrato', 'contratista', 'tipo', 'rol', 'proyecto', 'orden_compra',)
    search_fields = ('proyecto__codigo', 'proyecto__nombre', 'contratista__nombre', 'contratista__apellido1')
    ordering = ("proyecto", "contratista",)
    list_filter = ("tipo", "proyecto__nombre", "rol")


class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    search_fields = ('codigo', 'nombre')
    ordering = ('codigo', 'nombre')


admin.site.register(Incidencia, IncidenciaAdmin)
admin.site.register(Sprint, SprintAdmin)
admin.site.register(Contratista, ContratistaAdmin)
admin.site.register(Planificacion, PlanificacionAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Observacion, ObservacionAdmin)
admin.site.register(Contratacion, ContratacionAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
