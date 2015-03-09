# -*- coding: utf-8 -*-
import hashlib
import time

def get_sessionid(request):
    """
    Cria e retorna o session id caso ele não exista
    :return: sessionid <int>: id da sessão
    """
    if not 'sessionid' in request.session:
        hash = hashlib.sha1()
        hash.update(str(time.time()))
        sessionid = hash.hexdigest()[:-10]
        request.session['stid'] = sessionid

        return  sessionid
    else:
        return None
