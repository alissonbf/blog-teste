# -*- coding: utf-8 -*-
"""
------
Models
------

Arquivo de configuração dos modelos da aplicação blog

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
29/11/2014      29/11/2014
==============  ==================

**Classes**

"""
from django.db import models

class Post(models.Model):
    """  Post do blog """
    class Meta:
        ordering = ['-created_on',]
        verbose_name = u'Post'
        verbose_name_plural = u'Posts'
        
    titulo      = models.CharField(u'Titulo', max_length=100)        
    texto       = models.TextField(u'Texto')                

    created_on = models.DateTimeField(u'Criado em', auto_now_add=True)          
    updated_on = models.DateTimeField(u'Atualizado em', auto_now=True)

    def __unicode__(self):
        return self.titulo

class Categoria(models.Model):
    """ Categoria """

    nome = models.CharField(max_length=30)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='subcategorias')

    created_on = models.DateTimeField(u'Criado em', auto_now_add=True)
    updated_on = models.DateTimeField(u'Atualizado em', auto_now=True)

    def __unicode__(self):
        return "%s | %s" %(self.parent, self.nome)


class Cliente(models.Model):
    """  Clientes usado na autenticação por token """
    class Meta:
        ordering = ['-created_on',]
        verbose_name = u'Cliente'
        verbose_name_plural = u'Clientes'

    token       = models.CharField(max_length=40, null=False, blank=False)

    created_on = models.DateTimeField(u'Criado em', auto_now_add=True)
    updated_on = models.DateTimeField(u'Atualizado em', auto_now=True)

    def __unicode__(self):
        return self.token


from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)