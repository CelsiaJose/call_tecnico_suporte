from django.test import TestCase
from django.contrib.auth.models import User
from chamados.models import Chamados

class TestChamadosTesteCase(TestCase):
    def setUp(self):
        self.usuario=User.objects.create_user(
            username="cristina",
            password="2345678"
        )
    def test_criacao_valida_chamado(self):
        chamado=Chamados.objects.create(
        usuario=self.usuario,
        titulo="erro no servidor",
        descricao="erro ao fechar servidor"
        )
        self.assertIsNotNone(chamado.id)

        #Nao pode permitir criar chamado sem usuario tem que dar erro e ser erro isto é verdade entao passa

        #se o erro acontece o teste passa
    def test_criar_chamado_sem_usuario(self):
        with self.assertRaises(Exception):
            Chamados.objects.create(
            titulo="Sem usuário",
            descricao="Erro"
        )
    def test_statudefault_dever_ser_aberto(self):
        chamado=Chamados.objects.create(
            usuario=self.usuario,
            titulo='status default',
            descricao='sem informar o status o sistema atribui o Aberto por default'
        )
        #faça com  que o status seja por default Aberto
        self.assertEqual(chamado.status, "ABERTO")

    def test_prioridadedefault_dever_ser_Baixa(self):
        chamado=Chamados.objects.create(
            usuario=self.usuario,
            titulo='priodidade default',
            descricao='sem informar a prioridade  o sistema atribui o Baixo por default'
        )
        #faça com  que a prioridade seja por default Aberto
        self.assertEqual(chamado.prioridade, "BAIXA")

    def test_datas_automaticas(self):
        chamado = Chamados.objects.create(
            usuario=self.usuario,
            titulo="Datas",
            descricao="Teste"
    )

        self.assertIsNotNone(chamado.data_criacao)
        self.assertIsNotNone(chamado.atualizado_em)
    
    #O Testa passa sem tecnico

    def test_tecncio_deve_ser_opcional(self):
        chamado= Chamados.objects.create(
            usuario=self.usuario,
            titulo="Sem tecnico",
            descricao="Sem o tecnico precisa passar"    
        )
        self.assertIsNone(chamado.tecnico)

    
   #Status inválidos deve dar erro 
   #ojectos.create nao temos aqui porque este objecto nao sera salvo no banco
    def test_statu_invalido_devedar_erro(self):
        chamado=Chamados(
            usuario=self.usuario,
            titulo='status ivalidos',
            descricao='status invalidos devem dar erro',
            status='aberto'
        )
        with self.assertRaises(Exception):
            chamado.full_clean()

    def test_nao_quebrar_str(self):
        chamado = Chamados.objects.create(
        usuario=self.usuario,
        titulo="para nao quebrar str",
        descricao="str pode quebrar entao vou transformar o metodo em texto"
    )

        texto = str(chamado)
        self.assertIn("para nao quebrar str", texto)
    



        


      
       
        
    


        


