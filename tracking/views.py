from django.shortcuts import render


# Create your views here.

def incidencia_list(request):
    return render(request, 'incidencias/incidencia_list.html', {})
