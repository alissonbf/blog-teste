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

from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header

from models import Cliente

class ApiAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        try:
            cliente = Cliente.objects.get(token=auth[1])
        except Cliente.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token not found')

        return (cliente, None)
