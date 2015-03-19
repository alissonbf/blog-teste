# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('efeito', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'efeito/arquivos', verbose_name=b'File')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name': 'Arquivo',
                'verbose_name_plural': 'Arquivos',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='foto',
            options={'ordering': ['ordem'], 'verbose_name': 'Foto', 'verbose_name_plural': 'Fotos'},
        ),
    ]
