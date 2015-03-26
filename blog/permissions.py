# -*- coding: utf-8 -*-
"""
-----------
Permissions
-----------

Arquivo de configuração das permissões via rest framework da aplicação blog

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
25/03/2015      25/03/2015
==============  ==================

"""

from rest_framework import permissions

class IsApi(permissions.BasePermission):
    """
    Permite livre acesso para todos os usuarios autenticados
    """

    def has_permission(self, request, view):
        return True