# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-25 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0003_auto_20160725_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='url',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Ссылка'),
        ),
    ]
