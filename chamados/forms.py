from django import forms
from .models import Chamados

class formChamados(forms.ModelForm):
    class Meta:
        model=Chamados

        fields=['usuario','titulo','descricao','tecnico','prioridade', 'tempo_solucao']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'id': 'titulo',
                'name': 'titulo',
                'placeholder': 'Resumo curto do problema',
                'required': 'required',
                'type': 'text',
            }),

            'descricao': forms.Textarea(attrs={
                'id': 'descricao',
                'name': 'descricao',
                'placeholder': 'Descreva o problema com o máximo de detalhes',
                'required': 'required',
                'rows': 4,
            }),
                

        }
     
        