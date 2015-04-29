# -*- coding: utf-8 -*-
"""
------
Urls
------

Arquivo de configuração das urls da aplicação sessao

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
29/04/2015      29/04/2015
==============  ==================

"""


from django.conf.urls import patterns, url

urlpatterns = patterns('sessao.views',
    url(r'show-sessao/$', 'show_sessao', name='show-sessao'),
)