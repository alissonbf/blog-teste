# -*- coding: utf-8 -*-
"""
------
Views
------

Arquivo de configuração das views da aplicação apple

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
05/03/2015      05/03/2015
==============  ==================

"""
import urllib2
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view

from teste import settings

from appleapi import get_sessionid

@api_view(['POST'])
def validar_receipt(request):
    """
    Valida o receipt da apple e retorna uma sessão
    :param request: Requisição http
    :param apple_receipt <str>: Recibo de compra da apple
    :param device <str>: Sistema operacional do aparelho, IOS ou Android
    :return: response <json>: status da operação, sessionid, mensagem sobre o resultado da operação
    """

    sessionid = get_sessionid(request)
    response = {
        "status": "failure",
        "sessionid": sessionid
    }

    data = json.loads(request.body)
    if data['device'] == 'IOS':
        receipt_data = data['apple_receipt']
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
            status_request = "success"
            apple_status = 'Apple Error: 21007'
        elif settings.DEBUG == True and status == 21008:
            status_request = "success"
            apple_status = 'Apple Error: 21008'
        elif settings.DEBUG == True and status == 0:
            status_request = "success"
            apple_status = 'Apple Live Store Receipt Valid'
        elif settings.DEBUG == False and status == 0:
            status_request = "success"
            apple_status = 'Apple Sandbox Receipt Valid'
        else:
            status_request = "failure"
            sessionid = None
            apple_status = 'Apple Receipt Invalid'

        response = {
            "status": status_request,
            "sessionid": sessionid,
            "message": apple_status
        }

    elif data['device'] == 'AND':
        response = {
            "status": "failure",
            "sessionid": None,
            "message": "Device not IOS"
        }
    return Response(response)


