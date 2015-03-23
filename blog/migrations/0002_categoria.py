# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=30)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('parent', models.ForeignKey(related_name='subcategorias', blank=True, to='blog.Categoria', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
