# -*- coding: utf-8 -*-
"""
------
Models
------

Arquivo de configuração das modelos da aplicação blog

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
29/11/2014      29/11/2014
==============  ==================

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