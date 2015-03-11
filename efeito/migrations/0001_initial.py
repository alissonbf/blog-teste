# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.CharField(max_length=200, verbose_name='Imagem')),
                ('ordem', models.IntegerField(verbose_name='Ordem')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'ordering': ['-created_on'],
                'verbose_name': 'Foto',
                'verbose_name_plural': 'Fotoa',
            },
            bases=(models.Model,),
        ),
    ]
