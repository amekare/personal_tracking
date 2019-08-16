from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('incidencia/', views.incidencia_list, name='incidencia-list'),
    path('incidencia/<int:pk>/', views.incidencia_detail, name='incidencia-detail'),
    path('sprint/', views.sprint_list, name='sprint-list'),
    path('sprint/<int:pk>/', views.sprint_detail, name='sprint-detail'),
    path('planificacion/', views.planificacion_list, name='planificacion-list'),
    path('planificacion/<int:pk>/', views.planificacion_detail, name='planificacion-detail'),
    path('proyecto/', views.proyecto_list, name='proyecto-list'),
    path('proyecto/<int:pk>/', views.proyecto_detail, name='proyecto-detail'),

]