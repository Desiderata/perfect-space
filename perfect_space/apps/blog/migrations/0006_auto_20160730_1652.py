# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-30 13:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160729_1733'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-date_publication',), 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
        migrations.AddField(
            model_name='post',
            name='date_publication',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 30, 13, 52, 58, 480180, tzinfo=utc), help_text='Сортировка по этому полю', verbose_name='Дата публикации'),
            preserve_default=False,
        ),
    ]
