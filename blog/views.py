# -*- coding: utf-8 -*-
"""
------
Views
------

Arquivo de configuração das views da aplicação blog

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
29/11/2014      25/03/2015
==============  ==================

"""
import smtplib


from django.core import paginator

from django.shortcuts   import render_to_response
from django.template    import RequestContext

from django.contrib.auth.models     import User
from django.contrib.auth.decorators import login_required

from django.core.paginator      import Paginator, EmptyPage, PageNotAnInteger

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes


from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from permissions import IsApi
from authentication import ApiAuthentication

from models     import Post, Categoria
from serializers import PostSerializer
from forms      import FormUser, FormPost

def home(request):
    """ Pagina principal do site """

    posts_lista = Post.objects.all().order_by('-created_on')
    
    paginacao   = Paginator(posts_lista, 2)
    pagina      = request.GET.get('pagina')
    
    try:
        posts = paginacao.page(pagina)
    except PageNotAnInteger:        
        posts = paginacao.page(1) # Se a página não é um inteiro, entregar primeira página.
    except EmptyPage:        
        posts = paginacao.page(paginator.num_pages) # Se a página está fora do intervalo (por exemplo, 9999), entregar última página de resultados.    
    
    return render_to_response('blog/index.html',locals(),context_instance=RequestContext(request),)

def usuario(request):
    """ Pagina de cadastro de usuarios """
    
    if request.method == 'POST':
        form = FormUser(request.POST)
        
        if form.is_valid():
            novo_usuario = form.save()
            mensagem = "Usuário cadastrado com sucesso!"
            usuario = User.objects.get(email=novo_usuario.email)
    else: 
        form = FormUser()    
            
    return render_to_response('blog/usuario.html',locals(),context_instance=RequestContext(request),)

@login_required
def post(request):
    """ Pagina de cadastro de posts """
    
    if request.method == 'POST':
        form = FormPost(request.POST)
        
        if form.is_valid():
            novo_post = form.save()
            mensagem = "Post cadastrado com sucesso!"            
    else: 
        form = FormPost()    
    
    return render_to_response('blog/post.html',locals(),context_instance=RequestContext(request),)

def enviar_email(request):
    """ Pagina de envio de emails """

    smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()

    smtpserver.login('souzamelolarissa@gmail.com', '6b16ae55')
    smtpserver.sendmail('alisson.barbosa@pgplayer.com.br','souzamelolarissa@gmail.com', 'Teste envio de email.')
    smtpserver.close()

    return render_to_response('blog/email.html',locals(),context_instance=RequestContext(request),)

@api_view(['GET', 'POST'])
def all_posts(request):
    """ Retorna um json com todos os post cadastrados """

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

@api_view(['GET', 'PUT', 'DELETE'])
def get_post(request, pk):
    """ Realiza as operações de select, update e delete no post dono da pk """

    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@authentication_classes((ApiAuthentication, ))
@permission_classes((IsApi,))
def api_auth(request):
    """
    Autentica o usuario via rest framework
    :param request:
    :return: response<json> - Retorna todos os posts
    """
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    response = {
        "status": "success",
        "shows": serializer.data,
    }

    return Response(response)


def autorelacionamento(request):
    """
    Mostra as categorias criadas apartir de um autorecalionamento
    http://blog.naison.com.br/django/auto-relacionamento-no-django
    :param request: Requisição http
    :return: pagina com categoria
    """
    categorias = Categoria.objects.filter(parent=None)
    return render_to_response('blog/autorelacionamento.html', locals(), context_instance=RequestContext(request),)

