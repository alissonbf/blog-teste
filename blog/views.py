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
import smtplib


from django.conf import settings

from boto.s3.connection import S3Connection

from boto.s3.key import Key
from django.http import HttpResponse

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

def video(request):
    """
        Retorna um objeto HttpResponse, com o conteudo de um arquivo .m3u8, seguindo os padrões do HLS
    """

    conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)

    conn.lookup(settings.AWS_STORAGE_BUCKET_NAME)

    bucket = conn.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)

    k = Key(bucket)
    k.key = "hinata-sets-off-some-fireworks-mod.m3u8"
    s = k.get_contents_as_string()

    string = ''
    link = False
    count = 0
    for line in s.split('\n'):
        if link:
            line = line.strip()
            line = "generate_temp_url if-1"
            link = False
            count += 1
        if '#EXTINF' in line:
            link = True
        if '#EXT-X-TARGETDURATION' in line:
            line = line + '\n' + '#EXT-X-MEDIA-SEQUENCE:0'
        if '#EXT-X-KEY:METHOD=AES-128' in line:
            line = 'key.txt'
            line = "generate_temp_url if-4"
            line = '#EXT-X-KEY:METHOD=AES-128,URI="'+line+'"'
        string = string + line + '\n'

    response = HttpResponse(string, content_type='application/x-mpegURL')
    response['Content-Disposition'] = 'attachment; filename="index.m3u8"'
    return response