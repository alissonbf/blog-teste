# -*- coding: utf-8 -*-
"""
------
Models
------

Arquivo de configuração das modelos da aplicação card

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
03/12/2014      03/12/2014
==============  ==================

"""
import pycard

from django.db import models
from django.core.exceptions import ValidationError

from dicionarios import BANDEIRA_CHOICES,MESES_CHOICES, ANOS_CHOICES

class Card(models.Model):
    """  Cartão de Crédito """
    class Meta:
        ordering = ['-created_on',]
        verbose_name = u'Cartão de Credito'
        verbose_name_plural = u'Cartões de Credito'

    bandeira    = models.CharField(u'Bandeira', max_length=50, choices=BANDEIRA_CHOICES, blank=True, null=True)
    nome        = models.CharField(u'Nome no Cartão', max_length=100, blank=True, null=True)
    numero      = models.IntegerField(u'Número do cartão', max_length=20, blank=True, null=True)
    mes_val     = models.IntegerField(u'Validade', max_length=2, choices=MESES_CHOICES, blank=True, null=True)
    ano_val     = models.IntegerField(u'Validade', max_length=4, choices=ANOS_CHOICES, blank=True, null=True)
    cvc         = models.IntegerField(u'Código de Segurança', max_length=3, blank=True, null=True)

    created_on = models.DateTimeField(u'Criado em', auto_now_add=True)          
    updated_on = models.DateTimeField(u'Atualizado em', auto_now=True)

    def __unicode__(self):
        return self.nome            
