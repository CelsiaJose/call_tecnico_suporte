#Testar se os botoes estao relamente a mostrar os resultados esperados 
'''from django.test import TestCase
from django.contrib.auth import User
from django.models import Chamados

class test_botoes(TestCase):
    def setUp(self):
        self.usuario=User.create_user( username='celsia',password='123456789')
    

    def test_butoes_criate(self):
        self.client.login(username='celsia',password='123456789')
'''