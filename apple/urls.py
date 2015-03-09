# -*- coding: utf-8 -*-
"""
------
Urls
------

Arquivo de configuração das urls da aplicação apple

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
05/03/2015     05/03/2015
==============  ==================

"""


from django.conf.urls import patterns, url

urlpatterns = patterns('apple.views',
    url(r'validar-receipt/$', 'validar_receipt', name='validar_receipt')
)