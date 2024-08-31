# pacientes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro_paciente, name='cadastro_paciente'), #CADASTRAR PACIENTE
    path('listagem/', views.listagem_pacientes, name='listagem_pacientes'), #VER LISTA DE PACIENTES
    path('atualizar/<int:id>/', views.atualizar_paciente, name='atualizar_paciente'), #ATUALIZAR PACIENTE
    path('excluir/<int:id>/', views.excluir_paciente, name='excluir_paciente'),  #para excluir paciente
]
