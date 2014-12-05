# -*- coding: utf-8 -*-
"""
------
Views
------

Arquivo de configuração das views da aplicação card

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
04/12/2014      04/12/2014
==============  ==================

"""

from django.shortcuts   import render_to_response
from django.template    import RequestContext

from forms import FormCard

def card(request):
    """ Pagina de cadastro de cartão de crédito """
    
    if request.method == 'POST':
        form = FormCard(request.POST)
        
        if form.is_valid():
            new_card = form.save()
            mensagem = "Cartão de Crédito cadastrado com sucesso!"            
    else: 
        form = FormCard()
        
    return render_to_response('card/index.html',locals(),context_instance=RequestContext(request),)