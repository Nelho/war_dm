# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-13 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Territorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256)),
                ('descricao', models.CharField(max_length=256)),
                ('pontuacao', models.IntegerField()),
                ('bonus_max', models.IntegerField()),
                ('data_abertura', models.DateField()),
                ('data_encerramento', models.DateField()),
                ('repeticao', models.BooleanField(default=False)),
            ],
        ),
    ]