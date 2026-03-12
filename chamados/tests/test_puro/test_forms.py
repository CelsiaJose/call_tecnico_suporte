from django.test import TestCase
from django.contrib.auth.models import User
from chamados.models import Chamados
from chamados.forms import formChamados

class Test_ChamadoForm(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username="celsia",
            password="123456"
        )
    #Preenchendo formulario chamados 

    def test_form_valido(self):

        data =  {
            'usuario': self.user.id,
            'titulo': 'Erro no sistema',
            'descricao': 'Tela branca ao abrir',
            'prioridade': 'BAIXA',
            'tempo_solucao': 24
        }
        form =formChamados(data=data)
        print(form.errors)
        self.assertTrue(form.is_valid())

        #fiedl so envia os campos e ja data campos e os valores 

    def test_form_invalido(self):
         data =  {
            'usuario': self.user.id,
            'titulo': 'Erro no sistema',
            'descricao': 'Tela branca ao abrir',
        }
         form =formChamados(data=data)
         print(form.errors)
         self.assertFalse(form.is_valid())

    def test_titulo_obrigatorio(self):

          data =  {
            'usuario': self.user.id,
            'titulo': '',
            'descricao': 'Tela branca ao abrir',
            'prioridade': 'BAIXA',
            'tempo_solucao': 24
        }

          form = formChamados(data=data)

          self.assertFalse(form.is_valid())

    #so salva o formulario se todos os campos estiverem correctos

    def test_form_save(self):
        data =  {
            'usuario': self.user.id,
            'titulo': 'Erro no sistema',
            'descricao': 'Tela branca ao abrir',
            'prioridade': 'BAIXA',
            'tempo_solucao': 24
        }
        form =formChamados(data=data)
        print(form.errors)
        self.assertTrue(form.is_valid())

        chamado=form.save()
        #verificar se  a variavel armazenou os dados enviados ou salvou-os
        self.assertEqual(Chamados.objects.count(), 1)
          # verificar dados
        self.assertEqual(chamado.titulo, "Erro no sistema")
        self.assertEqual(chamado.usuario, self.user)

