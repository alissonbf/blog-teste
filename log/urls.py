# -*- coding: utf-8 -*-
"""
------
Urls
------

Arquivo de configuração das urls da aplicação log

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
25/05/2015      25/05/2015
==============  ==================

"""


from django.conf.urls import patterns, url

urlpatterns = patterns('log.views',
    url(r'debug/$', 'debug', name='debug'),
)