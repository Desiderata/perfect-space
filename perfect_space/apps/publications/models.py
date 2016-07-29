# coding=utf-8
import os
from django.db import models
from django.utils.datetime_safe import datetime
from django.utils.html import format_html
from easy_thumbnails.files import get_thumbnailer


class Publication(models.Model):
    COVER_WIDTH = 200
    COVER_HEIGHT = 274

    title_ru = models.CharField(blank=True, max_length=255, verbose_name='Заголовок')
    title_en = models.CharField(blank=True, max_length=255, verbose_name='Заголовок')
    description_ru = models.CharField(blank=True, max_length=1024, verbose_name='Описание')
    description_en = models.CharField(blank=True, max_length=1024, verbose_name='Описание')

    date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Дата', help_text='Сортировка по этому полю')
    url = models.CharField(max_length=255, blank=True, default='', verbose_name='Ссылка')
    cover = models.ImageField(upload_to='publications_cover/%Y/%m/%d/', verbose_name='Обложка', help_text='Размер превью 200х274')

    def __str__(self):
        return self.title_ru

    def save(self, *args, **kwargs):
        self.cover_resize()
        super().save(*args, **kwargs)

    def cover_preview(self):
        cover_url = self.cover.url if self.cover else ''
        return format_html('<img style="max-width: 100%" src="{0}" alt="" />', cover_url)
    cover_preview.short_description = 'Превью'

    def cover_resize(self):
        if not self.cover:
            return

        thumb = get_thumbnailer(self.cover.file, self.cover.file.name)
        cover = thumb.get_thumbnail({
            'size': (self.COVER_WIDTH, self.COVER_HEIGHT),
            'crop': True
        })
        self.cover.save(cover.name, cover.file, save=False)
        os.remove(cover.path)

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'


class PublicationImage(models.Model):
    IMAGE_WIDTH = 1920
    IMAGE_HEIGHT = 1200

    publication = models.ForeignKey(Publication, related_name='images', verbose_name='Публикация')
    image = models.ImageField(upload_to='publications_images/%Y/%m/%d/', blank=True, null=True, verbose_name='Изображение')

    def save(self, *args, **kwargs):
        self.image_resize()
        super().save(*args, **kwargs)

    def image_preview(self):
        image_url = self.image.url if self.image else ''
        return format_html('<img style="max-width: 100%" src="{0}" alt="" />', image_url)
    image_preview.short_description = 'Превью'

    def image_resize(self):
        if not self.image:
            return

        thumb = get_thumbnailer(self.image.file, self.image.file.name)
        image = thumb.get_thumbnail({
            'size': (self.IMAGE_WIDTH, self.IMAGE_HEIGHT),
            'crop': True
        })
        self.image.save(image.name, image.file, save=False)
        os.remove(image.path)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Изображение публикации'
        verbose_name_plural = 'Изображения публикации'
