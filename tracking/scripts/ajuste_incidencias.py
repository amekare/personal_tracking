from tracking.models import Incidencia


def update(*args):
    incidencias = Incidencia.objects.all()
    for incidencia in incidencias:
        incidencia.save()
