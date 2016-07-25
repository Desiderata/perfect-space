# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-25 11:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0004_publication_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicationimage',
            name='publication',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='publications.Publication', verbose_name='Публикация'),
        ),
    ]
