# -*- coding: utf-8 -*-
"""
------
Forms
------

Arquivo de configuração das formularios da aplicação card

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
04/12/2014      04/12/2014
==============  ==================

"""
import pycard

from django                     import forms

from models import Card

from dicionarios import BANDEIRA_CHOICES, MESES_CHOICES, ANOS_CHOICES

class FormCard(forms.ModelForm):
    """ Formulario de Cadastro de Usuarios"""
    class Meta:
        model = Card
        fields = ('bandeira','nome','numero','mes_val','ano_val','cvc',)
        
    bandeira    = forms.CharField(widget=forms.Select(choices=BANDEIRA_CHOICES),required=True,)    
    nome        = forms.CharField(required=True,)
    numero      = forms.IntegerField(required=True,)
    mes_val     = forms.IntegerField(label=False,widget=forms.Select(choices=MESES_CHOICES),required=True,)
    ano_val     = forms.IntegerField(label=False,widget=forms.Select(choices=ANOS_CHOICES),required=True,)
    cvc         = forms.IntegerField(label=u'Cód. de segurança',required=True)
    
    def clean_numero(self):
        """ Validação do cartão """
        
        card = pycard.Card(
            number=str(self.cleaned_data['numero']),
            month=int(self.data['mes_val']),
            year=int(self.data['ano_val']),
            cvc=int(self.data['cvc'])
        )        
        
        if not card.is_valid:
            raise forms.ValidationError('Cartão invalido.')

        return self.cleaned_data['numero']    
        
        
        
    
  
    