# -*- coding: utf-8 -*-
"""
------
Views
------

Arquivo de configuração das views da aplicação visao

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
11/05/2015      11/05/2015
==============  ==================

**Metodos**

"""

from django.shortcuts   import render_to_response
from django.template    import RequestContext

from visao.decorators import set_session_id, set_session_mg

@set_session_id(hash="Lorem ipsum")
@set_session_mg
def decorator(request):
    """ Mostra um post processado em um decorator """

    return render_to_response('visao/decorator.html', locals(), context_instance=RequestContext(request),)