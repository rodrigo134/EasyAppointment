from django.urls import path
from . import views


urlpatterns = [
    path('', views.pacientes, name = 'pacientes'),  #name é chamado tanto no formulario, quanto no redirect
    path('<int:id>', views.pacientes_view , name ='paciente_view')
]
