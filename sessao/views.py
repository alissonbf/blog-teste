# -*- coding: utf-8 -*-
"""
------
Views
------

Arquivo de configuração das views da aplicação sessao

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
29/04/2015      29/04/2015
==============  ==================

**Metodos**

"""

from django.shortcuts   import render_to_response
from django.template    import RequestContext
from sessao.utility import set_token


def show_sessao(request):
    """ Mostra as variaveis de sessão """
    request.session['msg'] = "Olá essa mensagem está na sessão."
    set_token(request)
    return render_to_response('sessao/show-sessao.html', locals(), context_instance=RequestContext(request),)