from django.contrib.auth.models import User
from chamados.serializers import ChamadoSerializer
from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse

class Test_authenticationjwt(TestCase):
    def setUp(self):
        self.usuario=User.objects.create_user(username='celsia',password='123456789')


#criar sessao para solicitar token 
    def test_login_para_token(self):

       
        url=reverse('token_obtain_pair')
        response = self.client.post(url,{
            "username": "celsia",
            "password": "123456789"
        })
        #print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)

  

    def test_login_para_token_invalido(self):
        url=reverse('token_obtain_pair')
        response=self.client.post(url,{
              "username": "celsia",
              "password": "senhaerrada"
        })
        self.assertEqual(response.status_code, 401)

    def test_acessar_pagina_protegida_token(self):
        #self.client = APIClient()
        url=reverse('token_obtain_pair')
        response = self.client.post(url,{
            'username':'celsia',
            'password':'123456789',
        })
        token = response.data["access"]
        url=reverse('chamado-list')
        response = self.client.get(url,HTTP_AUTHORIZATION=f'Bearer {token}')
        print(response.status_code)
        self.assertEqual(response.status_code,200)
       


