# -*- coding: utf-8 -*-
"""
------
Views
------

Arquivo de configuração das autenticações da aplicação blog

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
29/11/2014      25/03/2015
==============  ==================

"""
import json

from rest_framework import authentication
from rest_framework import exceptions

from models import Cliente

class ApiAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        data = json.loads(request.body)

        try:
            cliente = Cliente.objects.get(token=data['token'])
        except Cliente.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token not found')

        return (cliente, None)
