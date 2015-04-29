# -*- coding: utf-8 -*-
"""
------
Urls
------

Arquivo de configuração das urls da aplicação api

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

urlpatterns = patterns('api.views',
    url(r'^get-all-posts/$', 'get_all_posts', name='get-all-posts'),
    url(r'^auth-get-all-posts/$', 'auth_get_all_posts', name='auth-get-all-posts'),
    url(r'^auth-login/$', 'auth_login', name='auth-login'),
    url(r'^auth-logout/$', 'auth_logout', name='auth-logout'),
    url(r'^auth-session-get-all-posts/$', 'auth_session_get_all_posts', name='auth-session-get-all-posts'),
)