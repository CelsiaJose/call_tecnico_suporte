from django import forms
from .models import Chamados

class formChamadoseditar(forms.ModelForm):
    class Meta:
        model=Chamados

        fields=['usuario','titulo','descricao','tecnico','prioridade']