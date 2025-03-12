from django.urls import path
from . import views


urlpatterns = [
    path('', views.pacientes, name = 'pacientes'),  #name é chamado tanto no formulario, quanto no redirect
    path('<int:id>/', views.pacientes_view , name ='paciente_view'),
    path('atualizar_paciente/<int:id>/', views.atualizar_paciente , name ='atualizar_paciente'),
    path('excluir_consulta/<int:id>', views.excluir_consulta, name="excluir_consulta"),
]
