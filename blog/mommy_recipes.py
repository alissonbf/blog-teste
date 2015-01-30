# -*- coding: utf-8 -*-
"""
--------------
Mommy Recipes
--------------

Dados que são obrigatorios existirem para os testes funcionarem

Autores:

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>

Data:

==============  ==================
Criação         Atualização
==============  ==================
30/01/2015      30/01/2015
==============  ==================

"""

from model_mommy.recipe import Recipe
from blog.models import Post

post_tecnologia = Recipe(
    Post,
    titulo="Será? Diretor do Google diz que a Internet vai desaparecer",
)

post_culinaria = Recipe(
    Post,
    texto="Um outro prato criado na escola de culinária é Vietnamese Apple Kabob ( espetinho vietnamita de maçã) que combina abacaxi",
)