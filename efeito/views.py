# -*- coding: utf-8 -*-
"""
------
Views
------

Arquivo de configuração das views da aplicação efeito

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
11/03/2015      11/03/2015
==============  ==================

"""
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from django.shortcuts   import render_to_response
from django.template    import RequestContext

from models import Foto
from forms import FormArquivo

@csrf_exempt
def drag_and_drop(request):
    """ Pagina de objetos organizaveis via drop and drag """
    
    fotos = Foto.objects.all().order_by('ordem')

    if request.method == 'POST':
        new_order = request.body.replace("[", "").replace("]", "").replace('"', "")
        newdata = map(int, new_order.split(','))
        for order, id in enumerate(newdata):
            Foto.objects.filter(pk=id).update(ordem=order)

        return JsonResponse({'data': newdata})

    return render_to_response('efeito/index.html', locals(), context_instance=RequestContext(request),)


def progress_bar(request):
    """ Cadastro com barra de progresso """

    if request.method == 'POST':
        form = FormArquivo(request.POST, request.FILES)
        if form.is_valid():
            arquivo = form.save()
            return JsonResponse({"msg": form.errors, "error": False})
        else:
            return JsonResponse({"msg": form.errors, "error": True})

    else:
        form = FormArquivo()

    return render_to_response('efeito/progress_bar.html', locals(), context_instance=RequestContext(request),)