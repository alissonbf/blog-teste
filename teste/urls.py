# -*- coding: utf-8 -*-
"""
------
Urls
------

Este arquivo contem as configurações das urls do projeto

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
29/11/2014      29/11/2014
==============  ==================

---------------
"""

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# configuração dos arquivos estaticos
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'teste.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'blog.views.home', name='home'),
    
    url(r'^blog/', include('blog.urls')),
    
    url(r'^entrar/$', 'django.contrib.auth.views.login',{'template_name': 'entrar.html'}, 'entrar'),
    url(r'^sair/$', 'django.contrib.auth.views.logout', {'template_name': 'sair.html'}, 'sair'),
)

if settings.LOCAL:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
    
urlpatterns += staticfiles_urlpatterns()