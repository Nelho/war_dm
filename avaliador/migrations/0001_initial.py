# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-05 14:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gabinete_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regiao_correcao', models.CharField(choices=[('R1', '1º Região'), ('R2', '2º Região'), ('R3', '3º Região'), ('R4', '4º Região'), ('R5', '5º Região'), ('R6', '6º Região'), ('R7', '7º Região')], default='R1', max_length=2)),
                ('regiao', models.CharField(choices=[('R1', '1º Região'), ('R2', '2º Região'), ('R3', '3º Região'), ('R4', '4º Região'), ('R5', '5º Região'), ('R6', '6º Região'), ('R7', '7º Região')], default='R1', max_length=2)),
                ('foto', models.ImageField(upload_to='fotos/')),
                ('tipo_usuario', models.CharField(choices=[('GR', 'MCE'), ('GR', 'MCEA'), ('GR', 'Grande Conselho'), ('AV', 'MCR')], default='AV', max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'gabinete_user',
            },
        ),
    ]