# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-25 11:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interiors', '0002_auto_20160624_1408'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interior',
            options={'ordering': ('-date_publication',), 'verbose_name': 'Интерьер', 'verbose_name_plural': 'Интерьеры'},
        ),
    ]
