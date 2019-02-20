from django.urls import path
from . import views

urlpatterns = [
    path('incidencia/', views.incidencia_list, name='incidencia-list'),
    path('incidencia/<int:pk>/', views.incidencia_detail, name='incidencia-detail'),
    path('sprint/', views.sprint_list, name='sprint-list'),
    path('sprint/<int:pk>/', views.sprint_detail, name='sprint-detail'),
    path('planificacion/', views.planificacion_list, name='planificacion-list'),
    path('planificacion/<int:pk>/', views.planificacion_detail, name='planificacion-detail'),

]