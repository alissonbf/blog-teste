# -*- coding: utf-8 -*-
"""
------
Views
------

Arquivo de configuração das views da aplicação galeria

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
03/02/2015      03/02/2015
==============  ==================

"""

from django.shortcuts   import render_to_response
from django.template    import RequestContext

from models import Galeria, Imagem

def galeria(request):
    """
        Pagina inicial das galerias de imagens
    """
    galerias = Galeria.objects.all()
    imagens = Imagem.objects.all()

    return render_to_response('galeria/index.html',locals(),context_instance=RequestContext(request),)