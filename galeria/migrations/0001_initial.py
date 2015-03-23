# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('arquivo', filebrowser.fields.FileBrowseField(max_length=200, null=True, verbose_name='Arquivo', blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'ordering': ['-created_on'],
                'verbose_name': 'Arquivo',
                'verbose_name_plural': 'Arquivos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, null=True, verbose_name='Nome', blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'ordering': ['-created_on'],
                'verbose_name': 'Galeria',
                'verbose_name_plural': 'Galerias',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, null=True, verbose_name='Nome', blank=True)),
                ('arquivo', models.ImageField(upload_to=b'galeria/imagem', null=True, verbose_name='Arquivo', blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'ordering': ['-created_on'],
                'verbose_name': 'Imagem',
                'verbose_name_plural': 'Imagens',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='arquivo',
            name='galeria',
            field=models.ForeignKey(related_name='arquivo', to='galeria.Galeria'),
            preserve_default=True,
        ),
    ]
