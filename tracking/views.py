from django.shortcuts import render
from .models import Incidencia


# Create your views here.

def incidencia_list(request):
    incidencias = Incidencia.objects.order_by('codigo')
    return render(request, 'incidencias/incidencia_list.html', {'incidencias':incidencias})
