# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-16 01:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capitulo', '0002_auto_20171016_0123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='capitulo_user',
            options={'permissions': (('pode_cadastrar_relatorio', 'Pode cadastrar relatório'),)},
        ),
    ]
