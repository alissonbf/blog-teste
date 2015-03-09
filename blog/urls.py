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

    url(r'^all-posts', 'all_posts', name='all_posts'),
    url(r'^get-post/(?P<pk>[0-9]+)/$', 'get_post', name='get_post'),

    url(r'^enviar-email/$', 'enviar_email', name='enviar_email'),
    url(r'video/$', 'video', name='video')
)