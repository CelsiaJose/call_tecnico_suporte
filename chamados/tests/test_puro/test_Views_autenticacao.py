'''Testes de Autenticação / Usuário e test de views

Login com credenciais corretas → deve passar

Login com senha errada → deve falhar

Logout funciona corretamente

Usuário não autenticado → não pode acessar páginas restritas

Refresh / JWT se você usar tokens'''
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

#from chamados.models import Chamados

class Test_de_autenticacao(TestCase):
    #criar usuario
    def setUp(self):
        self.usuario=User.objects.create_user(
            username="celsia",
            password="123456789")

    #testar no navegar se o usario pode ou nao entrar no sistema
    def test_login_valido(self):

        login = self.client.login(
             username="celsia",
             password="123456789"
        )
        self.assertTrue(login)

    def test_login_invalido(self):
        login=self.client.login(
            username='celsia',
            password='125874'
        )
        self.assertFalse(login)

#simular a pagina de listar e que precise de usuario 
#Usuario nao logado nao ve pagina de listagem
#Usuario logado ve pagina de login
    def test_pagina_protegida(self):
        login_ok = self.client.login(
        username="celsia",
        password="123456789"
    )
        self.assertTrue(login_ok)  
        
        url=reverse('chamado_listar')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        print(response.status_code)
    
    #Pagina protegida e usuario sem login antes
    def test_pagina_protegida_anonimoUser(self):
        url=reverse('chamado_listar')
        response=self.client.get(url)
        self.assertNotEqual(response.status_code,200)

    def test_pagina_protegida_redirect(self):
        url=reverse('chamado_listar')
        response=self.client.get(url)
        #self.assertEqual(response.status_code,302)
        self.assertRedirects(response,f"/accounts/login/?next={url}")

    #Testar Logout funciona corretamente
    #testar todas as views protegidas
    #jwt é testado a nivel de django puro ou api

    def test_criar_chamado(self):
        login=self.client.login(
            username='celsia',
            password='23456789'
        )


