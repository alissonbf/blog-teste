# -*- coding: utf-8 -*-
"""
------
Urls
------

Arquivo de configuração das urls da aplicação evento

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
11/03/2015      11/03/2015
==============  ==================

"""


from django.conf.urls import patterns, url

urlpatterns = patterns('efeito.views',
    url(r'drag-and-drop/$', 'drag_and_drop', name='drag_and_drop'),
    url(r'progress-bar/$', 'progress_bar', name='progress_bar'),
)