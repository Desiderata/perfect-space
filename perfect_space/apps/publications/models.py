# coding=utf-8
from django.db import models
from django.utils.html import format_html


class Publication(models.Model):
    title_ru = models.CharField(blank=True, max_length=255, verbose_name='Заголовок')
    title_en = models.CharField(blank=True, max_length=255, verbose_name='Заголовок')
    description_ru = models.CharField(blank=True, max_length=1024, verbose_name='Описание')
    description_en = models.CharField(blank=True, max_length=1024, verbose_name='Описание')

    file = models.FileField(upload_to='publications/%Y/%m/%d/', verbose_name='Файл')
    cover = models.ImageField(upload_to='publications_cover/%Y/%m/%d/', verbose_name='Обложка')

    def __str__(self):
        return self.title_ru

    def cover_preview(self):
        cover_url = self.cover.url if self.cover else ''
        return format_html('<img src="{0}" alt="" />', cover_url)
    cover_preview.short_description = 'Превью'

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
