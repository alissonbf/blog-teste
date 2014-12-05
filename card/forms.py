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
    cvc         = forms.CharField(label=u'Cód. de segurança',max_length=4,min_length=3,required=True)
    
    def clean_numero(self):
        """ Validação do cartão """
        
        card = pycard.Card(
            number=str(self.cleaned_data['numero']),
            month=int(self.data['mes_val']),
            year=int(self.data['ano_val']),
            cvc=int(self.data['cvc'])
        )        
        
        if not card.is_mod10_valid:
            raise forms.ValidationError('Cartão invalido. Verifique se digitou todos os dados corretamente')

        return self.cleaned_data['numero']    

    def clean_mes_val(self):
        """ Validação do cartão """
        
        card = pycard.Card(
            number=str(self.data['numero']),
            month=int(self.cleaned_data['mes_val']),
            year=int(self.data['ano_val']),
            cvc=int(self.data['cvc'])
        )            

        if card.is_expired:
            raise forms.ValidationError('Data de validade do cartão expirou.')

        return self.cleaned_data['mes_val']        
        
        
    
  
    