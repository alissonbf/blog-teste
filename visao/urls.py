# -*- coding: utf-8 -*-
"""
------
Urls
------

Arquivo de configuração das urls da aplicação visao

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
11/05/2015      11/05/2015
==============  ==================

"""


from django.conf.urls import patterns, url

urlpatterns = patterns('visao.views',
    url(r'decorator/$', 'decorator', name='decorator'),
)