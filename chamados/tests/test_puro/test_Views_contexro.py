from django.test import TestCase
from django.contrib.auth.models import User
from chamados.models import Chamados
from django.urls import reverse


#O objectivo e testar a criacao dos novos chamados e se estao sendo exibidos
class test_views_contestcase(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username="celsia",
            password="123456789"
        )
        #criando chamado e adicionando na base test
        self.chamado1=Chamados.objects.create(
            usuario=self.user,
            titulo='novo chamado',
            descricao='testando criacao e exibicao de chamado'  
        )
        self.chamado2 = Chamados.objects.create(
            titulo="Erro sistema",
            descricao="Tela branca",
            usuario=self.user
        )

    def test_chamados_criado_addlist(self):
        #mostra-los na listagem 
        self.client.login(username='celsia',password='123456789')
        url=reverse('chamado_listar')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

        #Parte crucial verificar se o Chamado criado aparece no contesto
        #este verficacao é a nivel da pagina renderizada e quem a exibe em html é o objecto criado chamaod 
        
        self.assertIn('chamados', response.context)

         # 3 Verificar quantidade
        self.assertEqual(len(response.context['chamados']), 2)
        #print(response.content.decode())

        #Verificar se um objeto específico está na lista
        self.assertContains(response, "Erro sistema")

        
