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
from django.views.generic import TemplateView

admin.autodiscover()

# configuração dos arquivos estaticos
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# configuração do filebrowser
from filebrowser.sites import site

urlpatterns = patterns('',
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'blog.views.home', name='home'),
    
    url(r'^blog/', include('blog.urls')),
    url(r'^card-credit/', include('card.urls')),
    url(r'^galeria/', include('galeria.urls')),
    url(r'^apple/', include('apple.urls')),
    url(r'^efeito/', include('efeito.urls')),

    url(r'^entrar/$', 'django.contrib.auth.views.login',{'template_name': 'entrar.html'}, 'entrar'),
    url(r'^sair/$', 'django.contrib.auth.views.logout', {'template_name': 'sair.html'}, 'sair'),

    url(r'^search/', include('haystack.urls')),
    url(r'^blog-teste-doc/$', TemplateView.as_view(template_name='grp_doc/change_form.html'), name="blog_teste_doc_index"),
)

if settings.LOCAL:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
    
urlpatterns += staticfiles_urlpatterns()