# -*- coding: utf-8 -*-
"""
========
AppleApi
========

Arquivo de configuração dos metodos para interação com a api da apple

Autores:

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>

.. cssclass:: table-bordered

==============  ==================
Criação         Atualização
==============  ==================
05/03/2015      05/03/2015
==============  ==================

-------
Metodos
-------


"""
import hashlib
import time

def get_sessionid(request):
    """
        Cria e retorna o session id caso ele não exista

        :rtype: int
    """
    if not 'sessionid' in request.session:
        hash = hashlib.sha1()
        hash.update(str(time.time()))
        sessionid = hash.hexdigest()[:-10]
        request.session['stid'] = sessionid

        return  sessionid
    else:
        return None
