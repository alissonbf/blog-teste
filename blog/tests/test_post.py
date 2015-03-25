# -*- coding: utf-8 -*-
"""
------------
Post's Tests
------------

Testes das funcionalidade POSTS, da aplicação blog

Autores:

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>

Data:

==============  ==================
Criação         Atualização
==============  ==================
29/01/2015      29/01/2015
==============  ==================

"""
import json

from model_mommy import mommy

from django.test                import TestCase
from django.test.client         import Client

from django.contrib.auth.models     import User
from django.core.urlresolvers       import reverse

from rest_framework.authtoken.models import Token

from blog.models import Post, Cliente
from blog.forms  import FormUser

class PostTestCase(TestCase):
    """
        Testes das funcionalidade POSTS
    """

    @classmethod
    def setUp(cls):
        """
            Prepara o terreno em que os testes irão trabalhar
        """
        cls.client = Client()

    @classmethod
    def tearDown(cls):
        """
            Finaliza a bagunça feita, se necessário
        """
        pass

    def testViewPostProtect(self):
        """
            Caso de Teste: A Página de Publicação só pode ser acessada se tiver um login ativado
        """
        response = self.client.get(reverse('post'), follow=True)
        self.assertRedirects(response, reverse('entrar')+'?next=/blog/cadastro-post/', status_code=302, target_status_code=200)

    def testMakeBasic(self):
        """
            Testa a criação de dados via model mommy com make basico
        """
        post = mommy.make(Post)
        self.assertEquals(Post.objects.count(), 1)

    def testMakeOverwritten(self):
        """
            Testa o make com sobrescrita
        """
        new_titulo = "Será? Diretor do Google diz que a Internet vai desaparecer"
        post = mommy.make(Post, titulo=new_titulo)
        self.assertEquals(post.titulo, new_titulo)

    def testPrepareBasic(self):
        """
            Testa o prepare basico
        """
        post = mommy.prepare(Post)
        self.assertEquals(Post.objects.count(), 0)

    def testMakeMany(self):
        """
            Testa o make com varios objetos
        """
        post = mommy.make(Post, _quantity=5)
        self.assertEquals(Post.objects.count(), 5)

    def testRecipe(self):
        """
            Testa o Recipe do model mommy
        """
        post = mommy.make_recipe('blog.post_tecnologia')
        self.assertEquals(post.titulo, "Será? Diretor do Google diz que a Internet vai desaparecer",)

    def testObjetosCreated(self):
        """ Caso de Teste: Cadastro de Usuarios e Post """
        self.usuario  = User.objects.get_or_create(username='teste')
        self.post     = Post.objects.get_or_create(titulo='Lorem ipsum', texto='Ferri accumsan deterruisset et duo, per cu omnes nostrud officiis, id duo delenit molestiae.')

        self.assertEquals(User.objects.count(), 1)
        self.assertEquals(Post.objects.count(), 1)

    def testFormUserEmpty(self):
        """
            Testa as respostas do servidor para um formulario vazio
        """
        vazio = {'first_name':'','last_name':'','email':'','username':'','password':'','confirme_a_senha':'',}
        test_vazio = FormUser(data=vazio)
        self.assertEqual(test_vazio.errors['first_name'],[u'Este campo é obrigatório.'])
        self.assertEqual(test_vazio.errors['last_name'],[u'Este campo é obrigatório.'])
        self.assertEqual(test_vazio.errors['email'],[u'Este campo é obrigatório.'])
        self.assertEqual(test_vazio.errors['username'],[u'Este campo é obrigatório.'])
        self.assertEqual(test_vazio.errors['password'],[u'Este campo é obrigatório.'])

    def testFormUserValid(self):
        """
            Testa o formulario valido
        """
        valido = {'first_name':'Luana','last_name':'Costa Araujo','email':'luana@gmail.com','username':'luana','password':'123','confirme_a_senha':'123',}
        test_valido = FormUser(data=valido)
        self.assertTrue(test_valido.is_valid())

    def testFormUserEmailInvalid(self):
        """
            Testa o formulario com email invalido
        """
        email = {'first_name':'Luana','last_name':'Costa Araujo','email':'luana.com','username':'luana','password':'123','confirme_a_senha':'123',}
        test_email = FormUser(data=email)
        self.assertEqual(test_email.errors['email'],[u'Informe um endereço de email válido.'])

    def testFormUserCapitalized(self):
        """
            Testa se a primeira letra do nome e sobrenome em caixa alta
        """
        nome = {'first_name':'luana','last_name':'costa araujo','email':'luana@gmail.com','username':'luana','password':'123','confirme_a_senha':'123',}
        test_nome = FormUser(data=nome)
        self.assertEqual(test_nome.errors['first_name'],[u'O nome deve começar com letra maiuscula.'])
        self.assertEqual(test_nome.errors['last_name'],[u'O sobrenome deve começar com letra maiuscula.'])

    def testFormUserPasswordIncorrect(self):
        """
            Testa a confirmação de senha errada
        """
        senha = {'first_name':'luana','last_name':'costa araujo','email':'luana@gmail.com','username':'luana','password':'123','confirme_a_senha':'123456',}
        test_senha = FormUser(data=senha)
        self.assertEqual(test_senha.errors['confirme_a_senha'],[u'Confirmacao de senha não confere!'])

    def testAllPostsView(self):
        """
            Testa o retorno da view all_posts
        """
        mommy.make(Post)
        response = self.client.get(reverse('all_posts'), content_type="application/json")
        resposta = json.loads(response.content)
        self.assertEquals(resposta['status'], "success")

    """
    def testAuthorizationSuccess(self):
        user = User.objects.create_user('foo', 'foo@bar.de', 'bar')
        token = Token.objects.get(user=user).key
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format(token)}
        response = self.client.get(reverse('api_auth'), {}, **header)
        self.assertEqual(response.status_code, 200, response.content)


    def testAuthorizationFailure(self):
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format('asdfasdfasdasdasdf')}
        response = self.client.get(reverse('api_auth'), {}, **header)
        self.assertEqual(response.status_code, 401, response.content)
    """
    def testAuthorizationCustomSuccess(self):
        cliente = mommy.make(Cliente)
        header = {'HTTP_AUTHORIZATION': 'Token {}'.format(cliente.token)}
        response = self.client.get(reverse('api_auth'), {}, **header)
        self.assertEqual(response.status_code, 20, response.content)