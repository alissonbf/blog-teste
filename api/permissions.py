# -*- coding: utf-8 -*-
"""
-----------
Permissions
-----------

Arquivo de configuração das permissões via rest framework da aplicação api

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

from rest_framework import permissions

class IsApi(permissions.BasePermission):
    """
        Permite livre acesso para todos os usuarios autenticados
    """

    def has_permission(self, request, view):
        return True