# -*- coding: utf-8 -*-
"""
------
Models
------

Arquivo de configuração das modelos da aplicação card

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
03/02/2015      03/02/2015
==============  ==================

"""


from django.db import models
from filebrowser.fields import FileBrowseField


class Galeria(models.Model):
    """
        Galeria de arquivos
    """
    class Meta:
        ordering = ['-created_on',]
        verbose_name = u'Galeria'
        verbose_name_plural = u'Galerias'

    nome        = models.CharField(u'Nome', max_length=100, blank=True, null=True)

    created_on = models.DateTimeField(u'Criado em', auto_now_add=True)          
    updated_on = models.DateTimeField(u'Atualizado em', auto_now=True)

    def __unicode__(self):
        return self.nome

EXTENSIONS = ['.jpg','.jpeg','.gif','.png',
             ]

class Arquivo(models.Model):
    """
        Arquivo da galeria
    """
    class Meta:
        ordering = ['-created_on',]
        verbose_name = u'Arquivo'
        verbose_name_plural = u'Arquivos'

    arquivo = FileBrowseField(u'Arquivo', max_length=200, directory="uploads/", extensions=EXTENSIONS, blank=True, null=True)
    galeria = models.ForeignKey(Galeria, related_name='arquivo')

    created_on = models.DateTimeField(u'Criado em', auto_now_add=True)
    updated_on = models.DateTimeField(u'Atualizado em', auto_now=True)