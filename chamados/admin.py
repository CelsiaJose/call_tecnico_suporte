from django.contrib import admin

# Register your models here.

from .models import Chamados

class ChamadoAdmin(admin.ModelAdmin):
    list_display = ('id','usuario', 'titulo','tecnico','prioridade', 'status','data_criacao','atualizado_em','tempo_solucao')
   
"""
      # colunas visíveis na lista
    search_fields = ('titulo', 'descricao')                 # campos pesquisáveis
    list_filter = ('status',)                               # filtros laterais
    ordering = ('-criado_em',)                              # ordenação padrão
"""
admin.site.register(Chamados, ChamadoAdmin)