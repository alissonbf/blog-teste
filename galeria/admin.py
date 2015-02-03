# -*- coding: utf-8 -*-
"""
------
Admin
------

Este arquivo contem a integração da aplicação django galeria com o admin do django

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
03/02/2015      03/02/2015
==============  ==================

---------------
"""

from django.contrib     import admin

from models import Arquivo, Galeria

class ArquivoInline(admin.TabularInline):
    """
        Formulario inline do arquivo
    """
    model   = Arquivo

class AdminGaleria(admin.ModelAdmin):
    """
        Configuração do django admin para a Galeria
    """
    list_display    = ('nome', 'created_on',)
    list_filter     = ('created_on',)
    search_fields   = ('nome', )

    inlines = [
        ArquivoInline,
    ]

admin.site.register(Galeria, AdminGaleria)