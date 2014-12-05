# -*- coding: utf-8 -*-
"""
------
Tests
------

Arquivo de configuração dos testes da aplicação card

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
03/12/2014      03/12/2014
==============  ==================

"""

from django.test                import TestCase
from django.test.client         import Client

from django.core.urlresolvers       import reverse

from models import Card
from forms  import FormCard

class CardTestCase(TestCase):
    """ Classe de teste da aplicação card """
    
    def setUp(self):
        """ prepara o terreno em que os testes irão trabalhar """        
        self.client = Client()

    def tearDown(self):
        """  finaliza a bagunça feita, se necessário """
        pass
    
    def testObjetosCriados(self):
        """ Caso de Teste: Cadastro de cartões de crédito """
        
        self.card = Card.objects.get_or_create(bandeira='visa',nome='Sofia S Fernandes', numero=4916475344022891, mes_val=12,ano_val=2016,cvc=891)        
        self.assertEquals(Card.objects.count(), 1)        
        
    def testUrlCard(self):
        """ Caso de Teste: Acesso ao cadastro de cartão de crédito """
        
        response = self.client.post(reverse('card'))
        self.assertEquals(response.status_code, 200)
        
    def testFormCard(self):
        """ Caso de Teste: Validação de cartão de credito """
        
        # Formulario vazio
        test_vazio = FormCard(data={'bandeira':'','nome':'','numero':'','validade':'','mes_val':'','ano_val':'','cvc':'',})
        self.assertEqual(test_vazio.errors['bandeira'],[u'Este campo é obrigatório.'])
        self.assertEqual(test_vazio.errors['nome'],[u'Este campo é obrigatório.'])
        self.assertEqual(test_vazio.errors['numero'],[u'Este campo é obrigatório.'])
        self.assertEqual(test_vazio.errors['mes_val'],[u'Este campo é obrigatório.'])
        self.assertEqual(test_vazio.errors['ano_val'],[u'Este campo é obrigatório.'])
        self.assertEqual(test_vazio.errors['cvc'],[u'Este campo é obrigatório.'])
        
        # Formulario correto
        test_correto = FormCard(data={'bandeira':'visa','nome':'Sofia S Fernandes','numero':4916475344022891,'mes_val':12,'ano_val':2016,'cvc':891,})
        self.assertTrue(test_correto.is_valid())        
        
        # Cartão de credito invalido
        test_cartao = FormCard(data={'bandeira':'visa','nome':'Sofia S Fernandes','numero':00000000001234123413241234,'mes_val':12,'ano_val':2016,'cvc':891,})
        self.assertEqual(test_cartao.errors['numero'],[u'Cartão invalido.'])
        
        # Cartão de credito valido
        test_cartao_valido = FormCard(data={'bandeira':'visa','nome':'Sofia S Fernandes','numero':4916475344022891,'mes_val':12,'ano_val':2016,'cvc':891,})
        self.assertTrue(test_cartao_valido.is_valid())
        
        
        
        
        