# -*- coding: utf-8 -*-
"""
------
Admin
------

Este arquivo contem a integração da aplicação django api com o admin do django

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

from django.contrib     import admin
from models             import Cliente

class AdminCliente(admin.ModelAdmin):
    """
        Configuração do formulario e exibição das informações no admin do django
    """
    list_display    = ('token', 'created_on', 'updated_on',)
    list_filter     = ('created_on',)
    search_fields   = ('token',)

admin.site.register(Cliente, AdminCliente)