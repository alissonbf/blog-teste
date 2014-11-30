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
29/11/2014      29/11/2014
==============  ==================

"""

from django.shortcuts   import render_to_response,redirect
from django.template    import RequestContext

from django.core.urlresolvers       import reverse
from django.contrib.auth.models     import User
from django.contrib.auth.decorators import login_required

from django.core.paginator      import Paginator, EmptyPage, PageNotAnInteger

from models     import Post

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