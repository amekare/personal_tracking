from django.shortcuts import render, get_object_or_404
from .models import Incidencia, Sprint, Planificacion, Observacion
from datetime import date


# Create your views here.

def index(request):
    no_activos = ['6', '7']

    activas = Planificacion.objects.filter(sprint__fecha_inicio__lte=date.today(),
                                           sprint__fecha_fin__gte=date.today()).exclude(
        incidencia__estado__in=no_activos).count()
    hechas = Incidencia.objects.filter(estado='6').count()
    sprint_activos = Sprint.objects.filter(fecha_inicio__lte=date.today(), fecha_fin__gte=date.today())
    return render(request, 'index.html', {'activas': activas, 'hechas': hechas, 'sprints': sprint_activos})


# Incidencias
def incidencia_list(request):
    incidencias = Incidencia.objects.order_by('codigo')
    return render(request, 'incidencia_list.html', {'incidencias': incidencias})


def incidencia_detail(request, pk):
    incidencia = get_object_or_404(Incidencia, pk=pk)
    observaciones = Observacion.objects.filter(planificacion__incidencia=incidencia)
    return render(request, 'incidencia_detail.html', {'incidencia': incidencia, 'observaciones': observaciones})


# Sprints
def sprint_list(request):
    sprints = Sprint.objects.order_by('numero')
    return render(request, 'sprint_list.html', {'sprints': sprints})


def sprint_detail(request, pk):
    sprint = get_object_or_404(Sprint, pk=pk)
    return render(request, 'sprint_detail.html', {'sprint': sprint})


# Planificacion
def planificacion_list(request):
    sprints = Sprint.objects.order_by('numero')
    return render(request, 'planificacion_list.html', {'sprints': sprints})


def planificacion_detail(request, pk):
    sprint = get_object_or_404(Sprint, pk=pk)
    planificaciones = Planificacion.objects.filter(sprint__pk=sprint.pk)
    return render(request, 'planificacion_detail.html',
                  {'sprint': sprint, 'planificaciones': planificaciones})
