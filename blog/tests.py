# -*- coding: utf-8 -*-
"""
------
Tests
------

Arquivo de configuração dos testes da aplicação blog

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
02/12/2014      03/12/2014
==============  ==================

"""

from django.test                import TestCase
from django.test.client         import Client

from django.contrib.auth.models     import User
from django.core.urlresolvers       import reverse

from models import Post
from forms  import FormUser

class BlogTestCase(TestCase):
    """ Classe de testes da aplicação blog """
    
    def setUp(self):
        """ prepara o terreno em que os testes irão trabalhar """
        
        self.client = Client()

    def tearDown(self):
        """  finaliza a bagunça feita, se necessário """
        pass        

    def testObjetosCriados(self):
        """ Caso de Teste: Cadastro de Usuarios e Post """
        
        self.usuario  = User.objects.get_or_create(username='teste')
        self.post     = Post.objects.get_or_create(titulo='Lorem ipsum', texto='Ferri accumsan deterruisset et duo, per cu omnes nostrud officiis, id duo delenit molestiae.')
        
        self.assertEquals(User.objects.count(), 1)
        self.assertEquals(Post.objects.count(), 1)
        
    def testProtecaoViewPost(self):
        """ Caso de Teste: A Página de Publicação só pode ser acessada se tiver um login ativado  """
            
        response = self.client.post(reverse('post'))
        self.assertEquals(response.status_code, 302)
        
    def testFormUser(self):
        """ Caso de Teste: Só aceitar emails válidos, Nome e Sobrenome devem manter a primeira letra Maiuscula e todos os campos são obrigadorios """
        
        # Formulario vazio
        vazio = {'first_name':'','last_name':'','email':'','username':'','password':'','confirme_a_senha':'',}
        test_vazio = FormUser(data=vazio)
        self.assertEqual(test_vazio.errors['first_name'],[u'Este campo é obrigatório.'])
        self.assertEqual(test_vazio.errors['last_name'],[u'Este campo é obrigatório.'])
        self.assertEqual(test_vazio.errors['email'],[u'Este campo é obrigatório.'])
        self.assertEqual(test_vazio.errors['username'],[u'Este campo é obrigatório.'])
        self.assertEqual(test_vazio.errors['password'],[u'Este campo é obrigatório.'])
        
        # Formulario valido
        valido = {'first_name':'Luana','last_name':'Costa Araujo','email':'luana@gmail.com','username':'luana','password':'123','confirme_a_senha':'123',}        
        test_valido = FormUser(data=vazio)
        self.assertFalse(test_valido.is_valid())
        
        # E-mail inválido
        email = {'first_name':'Luana','last_name':'Costa Araujo','email':'luana.com','username':'luana','password':'123','confirme_a_senha':'123',}
        test_email = FormUser(data=email)
        self.assertEqual(test_email.errors['email'],[u'Informe um endereço de email válido.'])
        
        # Primeira letra do nome e sobrenome em caixa alta
        nome = {'first_name':'luana','last_name':'costa araujo','email':'luana@gmail.com','username':'luana','password':'123','confirme_a_senha':'123',}            
        test_nome = FormUser(data=nome)        
        self.assertEqual(test_nome.errors['first_name'],[u'O nome deve começar com letra maiuscula.'])
        self.assertEqual(test_nome.errors['last_name'],[u'O sobrenome deve começar com letra maiuscula.'])
        
        # Confirmação de senha errada
        senha = {'first_name':'luana','last_name':'costa araujo','email':'luana@gmail.com','username':'luana','password':'123','confirme_a_senha':'123456',}                    
        test_senha = FormUser(data=senha)
        self.assertEqual(test_senha.errors['confirme_a_senha'],[u'Confirmacao de senha não confere!'])









