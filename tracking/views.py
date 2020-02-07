from django.shortcuts import render, get_object_or_404
from tracking.models import *
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
def planificacion_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    sprints = Sprint.objects.filter(proyecto__pk=proyecto.pk).order_by('-fecha_inicio')
    return render(request, 'planificacion_list.html', {'sprints': sprints, 'proyecto': proyecto})
    # planificaciones = Planificacion.objects.filter(contratacion__proyecto__pk=proyecto.pk).distinct().order_by(
    #     '-sprint__fecha_inicio')
    # return render(request, 'planificacion_list.html', {'planificaciones': planificaciones, 'proyecto': proyecto})


def planificacion_sprint(request, pk):
    sprint = get_object_or_404(Sprint, pk=pk)
    planificaciones = Planificacion.objects.filter(sprint__pk=sprint.pk)
    return render(request, 'planificacion_detail.html',
                  {'sprint': sprint, 'planificaciones': planificaciones})


# Proyectos

def proyecto_list(request):
    proyectos = Proyecto.objects.order_by('codigo')
    return render(request, 'proyecto_list.html', {'proyectos': proyectos})


def proyecto_detail(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    contrataciones = Contratacion.objects.filter(proyecto__pk=proyecto.pk)
    #planificaciones = Planificacion.objects.filter(incidencia__producto__contratacion__proyecto__pk=pk)
    sprints = Sprint.objects.filter(proyecto__pk = proyecto.pk)
    return render(request, 'proyecto_detail.html', {'proyecto': proyecto, 'contrataciones': contrataciones,
                                                    'sprints': sprints})


# Contratacion

def contratacion_list(request):
    contrataciones = Contratacion.objects.order_by('proyecto__codigo')
    return render(request, 'contratacion_list.html', {'contrataciones': contrataciones})


def contratacion_detail(request, pk):
    contratacion = get_object_or_404(Contratacion, pk=pk)
    productos = Producto.objects.filter(contratacion=contratacion)
    return render(request, 'contratacion_detail.html',
                  {'contratacion': contratacion, 'productos': productos})


def contratista_detail(request, pk):
    contratista = get_object_or_404(Contratista, pk=pk)
    contrataciones = Contratacion.objects.filter(contratista=contratista)
    return render(request, 'contratista_detail.html', {'contratista': contratista, 'contrataciones': contrataciones})
