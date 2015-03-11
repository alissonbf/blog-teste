# -*- coding: utf-8 -*-
"""
------
Admin
------

Este arquivo contem a integração da aplicação django efeito com o admin do django

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
11/03/2015      11/03/2015
==============  ==================

**Classes**

---------------
"""
from django.contrib     import admin
from models             import Foto

class AdminFoto(admin.ModelAdmin):
    """
        Configuração do formulario e exibição das informações no admin do django
    """
    list_display    = ('admin_image', 'ordem', 'created_on', 'updated_on',)
    
admin.site.register(Foto, AdminFoto)