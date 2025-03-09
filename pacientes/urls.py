from django.urls import path
from . import views


urlpatterns = [
    path('cadastrar/', views.pacientes, name = 'pacientes'),
]
