# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-05 14:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('capitulo', '0010_auto_20171004_0252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capitulo_User',
            fields=[
                ('numero', models.IntegerField(primary_key=True, serialize=False)),
                ('data_fundacao', models.DateField()),
                ('data_instalacao', models.DateField()),
                ('mestre_conselheiro', models.CharField(max_length=128)),
                ('regiao', models.CharField(choices=[('R1', '1º Região'), ('R2', '2º Região'), ('R3', '3º Região'), ('R4', '4º Região'), ('R5', '5º Região'), ('R6', '6º Região'), ('R7', '7º Região')], default='R1', max_length=2)),
                ('foto', models.ImageField(upload_to='fotos/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'capitulo_user',
            },
        ),
        migrations.RemoveField(
            model_name='usuariocapitulo',
            name='avaliador',
        ),
        migrations.RemoveField(
            model_name='usuariocapitulo',
            name='usuarioCap',
        ),
        migrations.RenameField(
            model_name='formulario',
            old_name='arquivozip',
            new_name='arquivo_zip',
        ),
        migrations.RenameField(
            model_name='formulario',
            old_name='dataEnvio',
            new_name='data_envio',
        ),
        migrations.RenameField(
            model_name='formulario',
            old_name='dataRealizacao',
            new_name='data_realizacao',
        ),
        migrations.RenameField(
            model_name='formulario',
            old_name='pontuacaoBonus',
            new_name='pontuacao_bonus',
        ),
        migrations.RemoveField(
            model_name='formulario',
            name='capituloUser',
        ),
        migrations.DeleteModel(
            name='UsuarioCapitulo',
        ),
        migrations.AddField(
            model_name='formulario',
            name='capitulo',
            field=models.ForeignKey(db_column='usuario_capitulo', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='capitulo_user', to='capitulo.Capitulo_User'),
            preserve_default=False,
        ),
    ]