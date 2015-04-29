# -*- coding: utf-8 -*-
"""
------
Views
------

Arquivo de configuração das views da aplicação api

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

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from blog.models     import Post

from api.models import Cliente
from api.serializers import PostSerializer
from api.authentication import ApiAuthentication, ApiSessionAuthentication
from api.permissions import IsApi


@api_view(['GET', 'POST'])
def get_all_posts(request):
    """
        Retorna um json com todos os post cadastrados
    """

    response = {
        "status": "failure",
    }

    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        response = {
            "status": "success",
            "shows": serializer.data,
        }
        return Response(response)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "status": "success",
                "shows": serializer.data,
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            "status": "failure",
            "errors": serializer.errors,
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    return Response(response)

@api_view(['GET', 'POST'])
@authentication_classes((ApiAuthentication, ))
@permission_classes((IsApi,))
def auth_get_all_posts(request):
    """
        Autentica o usuario via rest framework
        :return: response<json> - Retorna todos os posts
    """
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    response = {
        "status": "success",
        "shows": serializer.data,
    }

    return Response(response)

@api_view(['GET', 'POST'])
def auth_login(request):
    """
        Realiza o login de usuario da api
    """

    if request.method == 'GET':
        token = request.GET.get('token', '')

    try:
        cliente = Cliente.objects.get(token=token)
        request.session['cliente_token'] = cliente.token

        response = {"status": "success", "message": "Cliente autenticado!"}

    except Cliente.DoesNotExist:
        response = {"status": "failure", "message": "Token não existe!"}

    return Response(response)

@api_view(['GET', 'POST'])
def auth_logout(request):
    try:
        del request.session['cliente_token']
        response = {"status": "success", "message": "Você foi saiu do sistema."}
    except KeyError:
        response = {"status": "failure", "message": "Key não encontrada!"}

    return Response(response)

@api_view(['GET', 'POST'])
@authentication_classes((ApiSessionAuthentication, ))
@permission_classes((IsApi,))
def auth_session_get_all_posts(request):
    """
        Autentica o usuario via rest framework
        :return: response<json> - Retorna todos os posts
    """
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    response = {
        "status": "success",
        "shows": serializer.data,
    }

    return Response(response)
