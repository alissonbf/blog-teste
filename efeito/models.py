# -*- coding: utf-8 -*-
"""
------
Models
------

Arquivo de configuração dos modelos da aplicação efeito

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
11/03/2015      11/03/2015
==============  ==================

**Classes**

"""
from django.db import models

class Foto(models.Model):
    """  Foto do blog """
    class Meta:
        ordering = ['ordem',]
        verbose_name = u'Foto'
        verbose_name_plural = u'Fotos'

    img      = models.CharField(u'Imagem', max_length=200)
    ordem    = models.IntegerField(u'Ordem')

    created_on = models.DateTimeField(u'Criado em', auto_now_add=True)          
    updated_on = models.DateTimeField(u'Atualizado em', auto_now=True)

    def __unicode__(self):
        return self.img

    def admin_image(self):
        """
        Renderiza uma tag html no django admin
        :return: image <str>, tag html img
        """
        return '<img src="%s"/>' % self.img

    admin_image.allow_tags = True

class Arquivo(models.Model):
    """ Arquivo de upload """
    class Meta:
        ordering = ['pk']
        verbose_name = u'Arquivo'
        verbose_name_plural = u'Arquivos'

    file      = models.FileField('File', null=False, blank=False, upload_to='efeito/arquivos')

    created_on = models.DateTimeField(u'Criado em', auto_now_add=True)
    updated_on = models.DateTimeField(u'Atualizado em', auto_now=True)

    def __unicode__(self):
        return "arquivo %s" %(self.id)


