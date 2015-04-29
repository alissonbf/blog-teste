# -*- coding: utf-8 -*-
"""
---------------
Serializers
---------------

Arquivo de configuração das serializações da aplicação api

Autores:

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>

Data:

==============  ==================
Criação         Atualização
==============  ==================
29/04/2015      29/04/2015
==============  ==================

**Classes**

"""

from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    """
        Classe que serializa os dados dos Post's
    """
    class Meta:
        model = Post
        fields = ('titulo', 'texto', 'created_on', 'updated_on')

