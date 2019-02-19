from django.urls import path
from . import views

urlpatterns = [
    path('', views.incidencia_list, name='incidencia_list'),
]