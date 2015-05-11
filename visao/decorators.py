# -*- coding: utf-8 -*-
"""
-----------
Decorators
-----------

Arquivo de configuração dos decorators da aplicação visao

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
import hashlib

from functools import wraps

def set_session_id(hash):
    """
    Cria uma session id utilizando um hash
    :param hash: hash para criação da session id
    """
    def decorator(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            request.session['session_id'] = hashlib.sha224(hash).hexdigest()
            return func(request, *args, **kwargs)
        return inner
    return decorator

def set_session_mg(f):
    def wrap(request, *args, **kwargs):
        request.session['msg'] = "Mensagem processada em um decorator"
        return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap
