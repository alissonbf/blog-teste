# -*- coding: utf-8 -*-
"""
------
Forms
------

Arquivo de configuração das formularios da aplicação efeito

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
19/03/2015      19/03/2015
==============  ==================

"""
from django                     import forms

from models import Arquivo

class FormArquivo(forms.ModelForm):
    """ Formulario de Cadastro de Post"""
    class Meta:
        model = Arquivo
        fields = ('file', )

    file = forms.FileField(required=True)