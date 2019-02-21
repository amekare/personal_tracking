from django.shortcuts import render, get_object_or_404
from .models import Incidencia, Sprint, Planificacion, Observacion


# Create your views here.

def index(request):
    return render(request, 'index.html', {})


# Incidencias
def incidencia_list(request):
    incidencias = Incidencia.objects.order_by('codigo')
    return render(request, 'incidencia_list.html', {'incidencias': incidencias})


def incidencia_detail(request, pk):
    incidencia = get_object_or_404(Incidencia, pk=pk)
    observaciones = Observacion.objects.filter(planificacion__incidencia=incidencia)
    return render(request, 'incidencia_detail.html', {'incidencia': incidencia, 'observaciones':observaciones})


# Sprints
def sprint_list(request):
    sprints = Sprint.objects.order_by('numero')
    return render(request, 'sprint_list.html', {'sprints': sprints})


def sprint_detail(request, pk):
    sprint = get_object_or_404(Sprint, pk=pk)
    return render(request, 'sprint_detail.html', {'sprint': sprint})


# Planificacion
def planificacion_list(request):
    planificaciones = Planificacion.objects.all()
    return render(request, 'planificacion_list.html', {'planificaciones': planificaciones})


def planificacion_detail(request, pk):
    planificacion = get_object_or_404(Planificacion, pk=pk)
    sprint = get_object_or_404(Sprint, pk=planificacion.sprint.pk)
    planificaciones = Planificacion.objects.filter(sprint=sprint)
    return render(request, 'planificacion_detail.html', {'planificacion': planificacion, 'planificaciones':planificaciones})
