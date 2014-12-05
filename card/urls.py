# -*- coding: utf-8 -*-
"""
------
Urls
------

Arquivo de configuração das urls da aplicação blog

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
04/12/2014      04/12/2014
==============  ==================

"""


from django.conf.urls import patterns, include, url

urlpatterns = patterns('card.views',
    url(r'^$', 'card', name='card'),    
)