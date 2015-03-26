# -*- coding: utf-8 -*-
"""
--------
ApiApple
--------

Arquivo de configuração dos metodos para interação com a api da apple

Autores:

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>

Data:

==============  ==================
Criação         Atualização
==============  ==================
05/03/2015      26/03/2015
==============  ==================

**Metodos**

"""
import json
import urllib2

from teste import settings

def get_apple_validate(apple_receipt):
    """
    Valida o receipt da apple
    :return: retorna o mensagens de validação
    """
    receipt_data = apple_receipt
    password = settings.APPLE_SHARED_SECRET
    if settings.DEBUG == True:
        url = settings.APPLE_LIVE_STORE
    else:
        url = settings.APPLE_SANDBOX_STORE

    data = {"receipt-data": receipt_data, "password": password}
    headers = {'Content-Type': 'text/Json; charset=utf-8'}
    dataj = json.dumps(data)

    request = urllib2.Request(url, dataj, headers)
    response = urllib2.urlopen(request)
    response_json = json.loads(response.read())
    status = response_json['status']

    if settings.DEBUG == True and status == 21007:
        status_request = True
        apple_status = 'Apple Error: 21007'
    elif settings.DEBUG == True and status == 21008:
        status_request = True
        apple_status = 'Apple Error: 21008'
    elif settings.DEBUG == True and status == 0:
        status_request = True
        apple_status = 'Apple Live Store Receipt Valid'
    elif settings.DEBUG == False and status == 0:
        status_request = True
        apple_status = 'Apple Sandbox Receipt Valid'
    else:
        status_request = False
        apple_status = 'Apple Receipt Invalid'

    response = {
        "status": status_request,
        "message": apple_status
    }

    return response