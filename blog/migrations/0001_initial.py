# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('texto', models.TextField(verbose_name='Texto')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'ordering': ['-created_on'],
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
            bases=(models.Model,),
        ),
    ]
