# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-29 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160729_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='summary_en',
            field=models.CharField(blank=True, max_length=200, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='summary_ru',
            field=models.CharField(blank=True, max_length=200, verbose_name='Краткое описание'),
        ),
    ]