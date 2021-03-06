from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from datetime import date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView


# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:

        no_activos = ['6', '7']

        activas = Planificacion.objects.filter(sprint__fecha_inicio__lte=date.today(),
                                               sprint__fecha_fin__gte=date.today()).exclude(
            incidencia__estado__in=no_activos).count()
        hechas = Incidencia.objects.filter(estado='6').count()
        sprint_activos = Sprint.objects.filter(fecha_inicio__lte=date.today(), fecha_fin__gte=date.today())
        return render(request, 'index.html', {'activas': activas, 'hechas': hechas, 'sprints': sprint_activos})


# Incidencias
def incidencia_list(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        incidencias = Incidencia.objects.order_by('codigo')
        return render(request, 'incidencia_list.html', {'incidencias': incidencias})


def incidencia_detail(request, pk):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        incidencia = get_object_or_404(Incidencia, pk=pk)
        observaciones = Observacion.objects.filter(planificacion__incidencia=incidencia)
        return render(request, 'incidencia_detail.html', {'incidencia': incidencia, 'observaciones': observaciones})


# Sprints
def sprint_list(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        sprints = Sprint.objects.order_by('numero')
        return render(request, 'sprint_list.html', {'sprints': sprints})


def sprint_detail(request, pk):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        sprint = get_object_or_404(Sprint, pk=pk)
        return render(request, 'sprint_detail.html', {'sprint': sprint})


# Planificacion
def planificacion_proyecto(request, pk):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        proyecto = get_object_or_404(Proyecto, pk=pk)
        sprints = Sprint.objects.filter(proyecto__pk=proyecto.pk).order_by('-fecha_inicio')
        return render(request, 'planificacion_list.html', {'sprints': sprints, 'proyecto': proyecto})
        # planificaciones = Planificacion.objects.filter(contratacion__proyecto__pk=proyecto.pk).distinct().order_by(
        #     '-sprint__fecha_inicio')
        # return render(request, 'planificacion_list.html', {'planificaciones': planificaciones, 'proyecto': proyecto})


def planificacion_sprint(request, pk):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        sprint = get_object_or_404(Sprint, pk=pk)
        planificaciones = Planificacion.objects.filter(sprint__pk=sprint.pk)
        return render(request, 'planificacion_detail.html',
                      {'sprint': sprint, 'planificaciones': planificaciones})


def planificacion_contratacion(request, pk,contratacion):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        sprint = get_object_or_404(Sprint, pk=pk)
        planificaciones = Planificacion.objects.filter(sprint__pk=sprint.pk, incidencia__producto__contratacion=contratacion)
        print("llegue")
        return render(request, 'planificacion_detail.html',
                      {'sprint': sprint, 'planificaciones': planificaciones})


# Proyectos

def proyecto_list(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        proyectos = Proyecto.objects.order_by('codigo')
        return render(request, 'proyecto_list.html', {'proyectos': proyectos})


def proyecto_detail(request, pk):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        proyecto = get_object_or_404(Proyecto, pk=pk)
        contrataciones = Contratacion.objects.filter(proyecto__pk=proyecto.pk)
        # planificaciones = Planificacion.objects.filter(incidencia__producto__contratacion__proyecto__pk=pk)
        sprints = Sprint.objects.filter(proyecto__pk=proyecto.pk)
        return render(request, 'proyecto_detail.html', {'proyecto': proyecto, 'contrataciones': contrataciones,
                                                        'sprints': sprints})


# Contratacion

def contratacion_list(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        contrataciones = Contratacion.objects.order_by('proyecto__codigo')
        return render(request, 'contratacion_list.html', {'contrataciones': contrataciones})


def contratacion_detail(request, pk):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        contratacion = get_object_or_404(Contratacion, pk=pk)
        producto_list = Producto.objects.filter(contratacion=contratacion)
        page = request.GET.get('page', 1)
        paginator = Paginator(producto_list, 10)
        try:
            productos = paginator.page(page)
        except PageNotAnInteger:
            productos = paginator.page(1)
        except EmptyPage:
            productos = paginator.page(paginator.num_pages)

        planificacion_list = Planificacion.objects.filter(incidencia__producto__contratacion=contratacion)

        sprints_id = []
        for plan in planificacion_list:
            if plan.sprint.pk in sprints_id:
                pass
            else:
                sprints_id.append(plan.sprint.pk)

        sprint_list = Sprint.objects.filter(pk__in=sprints_id)
        page2 = request.GET.get('page', 1)
        paginator2 = Paginator(sprint_list, 10)
        try:
            sprints = paginator2.page(page2)
        except PageNotAnInteger:
            sprints = paginator2.page(1)
        except EmptyPage:
            sprints = paginator2.page(paginator2.num_pages)

        return render(request, 'contratacion_detail.html',
                      {'contratacion': contratacion, 'productos': productos, 'sprints':sprints})


def contratista_detail(request, pk):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        contratista = get_object_or_404(Contratista, pk=pk)
        contrataciones = Contratacion.objects.filter(contratista=contratista)
        return render(request, 'contratista_detail.html',
                      {'contratista': contratista, 'contrataciones': contrataciones})


def producto_detail(request, pk):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        producto = get_object_or_404(Producto, pk=pk)
        if producto.modificado:
            productohijo_list = Producto.objects.filter(padre=producto.pk)
            page = request.GET.get('page', 1)
            paginator = Paginator(productohijo_list, 10)
            try:
                incidencias = paginator.page(page)
            except PageNotAnInteger:
                incidencias = paginator.page(1)
            except EmptyPage:
                incidencias = paginator.page(paginator.num_pages)
        else:
            incidencia_list = Incidencia.objects.filter(producto=producto)
            page = request.GET.get('page', 1)
            paginator = Paginator(incidencia_list, 10)
            try:
                incidencias = paginator.page(page)
            except PageNotAnInteger:
                incidencias = paginator.page(1)
            except EmptyPage:
                incidencias = paginator.page(paginator.num_pages)

        return render(request, 'producto_detail.html', {'producto': producto, 'incidencias': incidencias})


def por_facturar(request, pk):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        contratacion = get_object_or_404(Contratacion, pk=pk)
        incidencia_list = Incidencia.objects.filter(producto__contratacion__pk=pk, estado=6, clasificacion=2).order_by('producto__numero')
        total_horas = list(incidencia_list.aggregate(Sum('horas_por_pagar')).values())[0]
        #agregar validación si viene none total_horas
        total_monto = total_horas * float(contratacion.pago_hora)
        page = request.GET.get('page', 1)
        paginator = Paginator(incidencia_list, 10)
        try:
            incidencias = paginator.page(page)
        except PageNotAnInteger:
            incidencias = paginator.page(1)
        except EmptyPage:
            incidencias = paginator.page(paginator.num_pages)
        return render(request, 'producto_pagar_list.html', {'contratacion': contratacion, 'incidencias': incidencias, 'total_horas': total_horas, 'total_monto': total_monto})


def update():
    incidencias = Incidencia.list.all()
    for incidencia in incidencias:
        incidencia.save()

