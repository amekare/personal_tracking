from django.shortcuts import get_object_or_404

from .models import Planificacion, Sprint


def load_planificacion(sprint_viejo_id, sprint_nuevo_id, fecha):
    estado_excepciones = ["5", "6", "7"]
    try:
        sprint_viejo = get_object_or_404(Sprint, pk=sprint_viejo_id)
        sprint_nuevo = get_object_or_404(Sprint, pk=sprint_nuevo_id)
    except Sprint.DoesNotExist:
        print("No se encontro al menos un sprint")
        sprint_viejo, sprint_nuevo = None

    if sprint_viejo and sprint_nuevo:

        planificaciones_viejas = Planificacion.objects.filter(sprint=sprint_viejo)
        contador = 0
        for plan in planificaciones_viejas:
            if plan.estado_fin not in estado_excepciones:
                if plan.estado_fin is None:
                    print(plan.__str__() + " sin estado final")
                else:
                    p = Planificacion.objects.filter(incidencia=plan.incidencia, sprint=sprint_nuevo)
                    if p.count() < 1:
                        planificacion = Planificacion()
                        planificacion.incidencia = plan.incidencia
                        planificacion.estado_inicio = plan.estado_fin
                        planificacion.sprint = sprint_nuevo
                        planificacion.fecha = fecha
                        planificacion.asignado = plan.asignado
                        planificacion.pago = plan.pago
                        planificacion.save()
                        contador = contador + 1
                        print(planificacion.__str__() + " agregado")
                    else:
                        print(p.__str__() + " ya existe")
            else:
                print(plan.__str__() + " no aplica, estado: " + plan.get_estado_fin_display())
        print("incidencias reasignadas: " + str(contador))
