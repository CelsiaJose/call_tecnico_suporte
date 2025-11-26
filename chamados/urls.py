from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('listar/', views.chamado_listar, name='chamado_listar'),
    path('criar/',views.chamados_Criar ,name='chamado_criar'),
    path('detalhe/<int:id>/',views.chamado_lista_detal,name='chamado_lista_detal'),
    path('editar/<int:id>/',views.chamado_editar,name='chamado_editar'),
    path('deletar/<int:id>/',views.chamado_deletar,name='chamado_deletar'),
    
]