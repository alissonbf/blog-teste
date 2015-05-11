# -*- coding: utf-8 -*-
"""
------
Views
------

Arquivo de configuração das views da aplicação chart

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
11/05/2015      11/05/2015
==============  ==================

**Metodos**

"""

from django.shortcuts   import render_to_response
from django.template    import RequestContext

def morris_charts(request):
    """ Mostra um grafico do Morris Charts """

    return render_to_response('chart/morris-charts.html', locals(), context_instance=RequestContext(request),)