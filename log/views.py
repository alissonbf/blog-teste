# -*- coding: utf-8 -*-
"""
------
Views
------

Arquivo de configuração das views da aplicação log

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
25/05/2015      25/05/2015
==============  ==================

**Metodos**

"""
import sys
import traceback
import logging

logger = logging.getLogger(__name__)

from django.core.exceptions import ObjectDoesNotExist

from django.shortcuts   import render_to_response
from django.template    import RequestContext

def debug(request):
    """ Cria um log de debug """

    titulo      = "Log"
    subtitulo   = "Cria um log"
    try:
        raise ObjectDoesNotExist
    except:
        logger.error(traceback.format_exc(sys.exc_info()[0]))

    return render_to_response('generic.html', locals(), context_instance=RequestContext(request),)
