# -*- coding: utf-8 -*-
"""
------
Admin
------

Este arquivo contem a integração da aplicação django card com o admin do django

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
04/12/2014      04/12/2014
==============  ==================

---------------
"""

from django.contrib     import admin
from models             import Card

class AdminCard(admin.ModelAdmin):
    """ Configuração do formulario e exibição das informações no admin do django """
    list_display    = ('bandeira','nome','numero','mes_val','ano_val','cvc')
    list_filter     = ('created_on',)    
    
admin.site.register(Card,AdminCard)