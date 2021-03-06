# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-25 11:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_auto_20160606_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicationImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='publications_images/%Y/%m/%d/', verbose_name='Изображение')),
                ('order', models.SmallIntegerField(default=0, verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Изображение публикации',
                'verbose_name_plural': 'Изображения публикации',
                'ordering': ('order',),
            },
        ),
        migrations.RemoveField(
            model_name='publication',
            name='file',
        ),
        migrations.AddField(
            model_name='publicationimage',
            name='publication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='publications.Publication', verbose_name='Публикация'),
        ),
    ]
