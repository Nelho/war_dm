# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-13 18:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capitulo', '0012_auto_20171013_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='territorio',
            field=models.ForeignKey(db_column='territorio', on_delete=django.db.models.deletion.CASCADE, related_name='territorio', to='mapa.Territorio'),
        ),
    ]
