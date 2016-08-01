# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-01 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160730_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='summary_en',
            field=models.TextField(blank=True, help_text='Выводится на странице блога (список постов)', max_length=200, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='summary_ru',
            field=models.TextField(blank=True, help_text='Выводится на странице блога (список постов)', max_length=200, verbose_name='Краткое описание'),
        ),
    ]
