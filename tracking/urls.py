from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('incidencia/', views.incidencia_list, name='incidencia-list'),
    path('incidencia/<int:pk>/', views.incidencia_detail, name='incidencia-detail'),
    path('sprint/', views.sprint_list, name='sprint-list'),
    path('sprint/<int:pk>/', views.sprint_detail, name='sprint-detail'),
    path('planificacion/proyecto/<int:pk>/', views.planificacion_proyecto, name='planificacion-list'),
    path('planificacion/<int:pk>/', views.planificacion_detail, name='planificacion-detail'),
    path('proyecto/', views.proyecto_list, name='proyecto-list'),
    path('proyecto/<int:pk>/', views.proyecto_detail, name='proyecto-detail'),
    path('contratacion/', views.contratacion_list, name='contratacion-list'),
    path('contratacion/<int:pk>/', views.contratacion_detail, name='contratacion-detail'),

]