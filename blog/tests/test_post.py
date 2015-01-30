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

from django.test                import TestCase
from django.test.client         import Client

from django.contrib.auth.models     import User
from django.core.urlresolvers       import reverse

from blog.models import Post

from model_mommy import mommy

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

    def testProtecaoViewPost(self):
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



