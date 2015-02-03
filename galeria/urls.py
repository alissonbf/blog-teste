# -*- coding: utf-8 -*-
"""
------
Urls
------

Arquivo de configuração das urls da aplicação galeria

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
03/02/2015      03/02/2015
==============  ==================

"""


from django.conf.urls import patterns, url

urlpatterns = patterns('galeria.views',
    url(r'^$', 'galeria', name='galeria'),
)