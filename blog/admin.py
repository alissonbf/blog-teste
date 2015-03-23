# -*- coding: utf-8 -*-
"""
------
Admin
------

Este arquivo contem a integração da aplicação django blog com o admin do django

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
29/11/2014      29/11/2014
==============  ==================

---------------
"""
from django.contrib     import admin
from models             import Post, Categoria

class AdminPost(admin.ModelAdmin):
    """
        Configuração do formulario e exibição das informações no admin do django
    """
    list_display    = ('titulo','texto','created_on','updated_on',)
    list_filter     = ('created_on',)
    search_fields   = ('titulo','texto',)

class AdminCategoria(admin.ModelAdmin):
    """
        Configuração do formulario e exibição das informações no admin do django
    """
    list_display    = ('nome', 'parent', 'created_on', 'updated_on',)
    list_filter     = ('created_on',)
    search_fields   = ('nome', 'texto',)

admin.site.register(Post, AdminPost)
admin.site.register(Categoria, AdminCategoria)