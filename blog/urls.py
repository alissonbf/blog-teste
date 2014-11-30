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
29/11/2014      29/11/2014
==============  ==================

"""


from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'^cadastro-usuario/$', 'usuario', name='usuario'),
    url(r'^cadastro-post/$', 'post', name='post'),
)