# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('img', models.ImageField(upload_to='', verbose_name='Portada')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre del proyecto')),
                ('status', models.CharField(choices=[('t', 'Terminado'), ('n', 'No terminado'), ('d', 'En desarrollo')], max_length=1, verbose_name='Estado')),
                ('year', models.SmallIntegerField(verbose_name='Año')),
                ('stack', models.CharField(max_length=255, verbose_name='Stack tecnológico')),
                ('responsive', models.BooleanField(default=True, verbose_name='RWD')),
                ('url', models.URLField(blank=True, verbose_name='Url del proyecto')),
                ('repository', models.URLField(blank=True, verbose_name='Url del repositorio')),
                ('published', models.BooleanField(default=False, verbose_name='Publicado')),
            ],
            options={
                'verbose_name_plural': 'Portafolio',
                'verbose_name': 'Portafolio',
            },
        ),
    ]