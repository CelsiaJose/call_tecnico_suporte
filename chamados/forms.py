from django import forms
from .models import Chamados
from django.contrib.auth.models import User
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
    # Antes de criar o form executa ainda esta funcao ou regras 
    def __init__(self,*args,**kwargs):
        #valida os dados e executa isto antes
        super().__init__(*args, **kwargs) #chama a classe pai forms.ModelForm
        #vai no campo técncio do formulario nao é do model é do form .query set ou seja me selciona apenas os usarios do grupo tencio
        self.fields['tecnico'].queryset = User.objects.filter(
         groups__name='tencios'
        )
     
        