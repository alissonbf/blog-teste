# -*- coding: utf-8 -*-
"""
------
Forms
------

Arquivo de configuração das formularios da aplicação blog

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
29/11/2014      29/11/2014
==============  ==================

"""
from django                     import forms
from django.contrib.auth.models import User

from models import Post

class FormUser(forms.ModelForm):
    """ Formulario de Cadastro de Usuarios"""
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password',)
        
    first_name       = forms.CharField(required=True,)    
    last_name        = forms.CharField(required=True,)
    email            = forms.CharField(required=True,)
    confirme_a_senha = forms.CharField(max_length=30, widget=forms.PasswordInput)
    password         = forms.CharField(max_length=30, widget=forms.PasswordInput)

    def clean_first_name(self):
        """ Este metodo valida se o nome começa com letra maiuscula """
        if not self.cleaned_data['first_name'].istitle():
            raise forms.ValidationError('O nome deve começar com letra maiuscula.')
        
        return self.cleaned_data['first_name']

    def clean_last_name(self):
        """ Este metodo valida se o sobrenome começa com letra maiuscula """
        if not self.cleaned_data['last_name'].istitle():
            raise forms.ValidationError('O sobrenome deve começar com letra maiuscula.')
        
        return self.cleaned_data['last_name']
    
    def clean_email(self):
        """ Este metodo verifica se o email é unico """
        if User.objects.filter(email=self.cleaned_data['email'],).count():
            raise forms.ValidationError('Já existe um usuario com este e-mail')

        return self.cleaned_data['email']

    def clean_confirme_a_senha(self):
        """ Este metodo verifica se o senha digitada no campo password é igual a digitada no campo confirme_a_senha """
        if self.cleaned_data['confirme_a_senha'] != self.data['password']:
            raise forms.ValidationError('Confirmacao de senha não confere!')

        return self.cleaned_data['confirme_a_senha']
    

    def save(self, commit=True):
        usuario = super(FormUser, self).save(commit=False)
        usuario.set_password(self.cleaned_data['password'])
        if commit:
            usuario.save()

        return usuario
    
class FormPost(forms.ModelForm):
    """ Formulario de Cadastro de Post"""
    class Meta:
        model = Post
        fields = ('titulo','texto',)
    
    texto = forms.Field(widget=forms.Textarea(attrs={'style':'height:200px;'}),required=True)
    