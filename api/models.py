# -*- coding: utf-8 -*-
"""
------
Models
------

Arquivo de configuração dos modelos da aplicação api

Autores:

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>

Data:

==============  ==================
Criação         Atualização
==============  ==================
29/04/2015      29/04/2015
==============  ==================

**Classes**

"""

from django.db import models

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
