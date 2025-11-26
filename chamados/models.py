from django.db import models
from django.contrib.auth.models import User
# Create your models here.

Prior_choices=[('BAIXA','Baixa'),
               ('MEDIA','Media'),
               ('ALTA','Alta')]

status_choices=[('ABERTO','Aberto'),
               ('Em_ANDAMENTO','Em_Andamento'),
               ('FEXADO','Fexado')]

class Chamados(models.Model):
    # apaga os registo models.PROTECT
    usuario=models.ForeignKey(User, related_name='usuarios', on_delete=models.CASCADE)
    titulo=models.CharField(max_length=200)
    descricao=models.TextField()
    tecnico = models.ForeignKey(User, related_name='tecnicos', on_delete=models.SET_NULL, null=True, blank=True)# apaga e mantem os chamados e deixa null
    prioridade = models.CharField(max_length=13, choices=Prior_choices, default='BAIXA')
    status=models.CharField(max_length=13 ,choices=status_choices,default='ABERTO')
    data_criacao=models.DateTimeField(auto_now_add=True)# nao aparece no form pois nao se edita é auto now
    atualizado_em = models.DateTimeField(auto_now=True)# nao aparece no form pois nao se edita é auto now
    tempo_solucao=models.IntegerField(default=24)

    def __str__(self):
        return self.titulo






