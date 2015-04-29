# -*- coding: utf-8 -*-
"""
---------------
Authentication
---------------

Arquivo de configuração das autenticações da aplicação api

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
29/04/2015      29/04/2015
==============  ==================

**Classes**

"""
import json

from rest_framework import authentication
from rest_framework import exceptions

from api.models import Cliente

class ApiAuthentication(authentication.BaseAuthentication):
    """
        Classe de altenticação da api
    """

    def authenticate(self, request):
        """
            Verifica se o token enviado existe no banco de dados
        """
        if request.method == 'GET':
            data = {'token': request.GET.get('token', '')}
        else:
            data = json.loads(request.body)

        try:
            cliente = Cliente.objects.get(token=data['token'])
        except Cliente.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token not found')

        return (cliente, None)

class ApiSessionAuthentication(authentication.BaseAuthentication):
    """
        Classe de altenticação da api usando sessions
    """

    def authenticate(self, request):
        """
            Verifica se os dados salvos na sessão são do usuario no banco de dados
        """
        try:
            cliente = Cliente.objects.get(token=request.session['cliente_token'])

        except Cliente.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token not found')
        except KeyError:
            raise exceptions.AuthenticationFailed('User unauthenticated')

        return (cliente, None)