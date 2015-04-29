# -*- coding: utf-8 -*-
"""
--------
Utility
--------

Arquivo de utilidades da aplicação sessao

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
import os
import binascii
import string
import random

def set_token(request):
    if 'user' in request.session:
        request.session['user']['token'] = binascii.hexlify(os.urandom(20)).decode()
    else:
        request.session['user'] = {'nome': ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(6)), 'token': binascii.hexlify(os.urandom(20)).decode()}
