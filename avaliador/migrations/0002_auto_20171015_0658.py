# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-15 06:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avaliador', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gabinete_user',
            options={'permissions': (('pode_avaliar_capitulo', 'Pode avaliar os relatórios dos capítulos'),)},
        ),
    ]