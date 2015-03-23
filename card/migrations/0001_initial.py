# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bandeira', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bandeira', choices=[(b'visa', b'VISA'), (b'mastercard', b'MasterCard')])),
                ('nome', models.CharField(max_length=100, null=True, verbose_name='Nome no Cart\xe3o', blank=True)),
                ('numero', models.IntegerField(max_length=20, null=True, verbose_name='N\xfamero do cart\xe3o', blank=True)),
                ('mes_val', models.IntegerField(blank=True, max_length=2, null=True, verbose_name='Validade', choices=[(1, b'Janeiro'), (2, b'Fevereiro'), (3, b'Mar\xc3\xa7o'), (4, b'Abril'), (5, b'Maio'), (6, b'Junho'), (7, b'Julho'), (8, b'Agosto'), (9, b'Setembro'), (10, b'Outubro'), (11, b'Novembro'), (12, b'Dezembro')])),
                ('ano_val', models.IntegerField(blank=True, max_length=4, null=True, verbose_name='Validade', choices=[(2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020)])),
                ('cvc', models.IntegerField(max_length=3, null=True, verbose_name='C\xf3digo de Seguran\xe7a', blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'ordering': ['-created_on'],
                'verbose_name': 'Cart\xe3o de Credito',
                'verbose_name_plural': 'Cart\xf5es de Credito',
            },
            bases=(models.Model,),
        ),
    ]
