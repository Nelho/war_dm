# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-04 01:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capitulo', '0004_formulario_arquivozip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formulario',
            old_name='arquivoZip',
            new_name='arquivozip',
        ),
    ]