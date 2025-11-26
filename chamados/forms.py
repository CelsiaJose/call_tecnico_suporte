from django import forms
from .models import Chamados

class formChamados(forms.ModelForm):
    class Meta:
        model=Chamados

        fields=['usuario','titulo','descricao','tecnico','prioridade', 'tempo_solucao']