# coding=utf-8
import os

from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.html import format_html
from easy_thumbnails.files import get_thumbnailer


class SEO(models.Model):
    title_ru = models.CharField(blank=True, max_length=255, verbose_name='Заголовок (title)')
    keywords_ru = models.CharField(blank=True, max_length=1024, verbose_name='Ключевые слова')
    description_ru = models.CharField(blank=True, max_length=1024, verbose_name='Описание')
    caption_ru = models.CharField(blank=True, max_length=255, verbose_name='Заголовок (h1)')

    title_en = models.CharField(blank=True, max_length=255, verbose_name='Заголовок (title)')
    keywords_en = models.CharField(blank=True, max_length=1024, verbose_name='Ключевые слова')
    description_en = models.CharField(blank=True, max_length=1024, verbose_name='Описание')
    caption_en = models.CharField(blank=True, max_length=255, verbose_name='Заголовок (h1)')

    class Meta:
        abstract = True


class Page(SEO):
    TEMPLATES = (
        ('index', 'Главная'),
        ('about', 'О Нас'),
        ('contacts', 'Контакты'),
        ('projects', 'Проекты'),
        ('interiors', 'Интерьеры'),
        ('blog', 'Блог'),
        ('blog_tags', 'Блог Теги'),
        ('search', 'Поиск'),
    )

    content_ru = models.TextField(blank=True, verbose_name='Текст')
    content_en = models.TextField(blank=True, verbose_name='Текст')

    slug = models.SlugField(max_length=100, db_index=True, unique=True, verbose_name='Псевдоним')
    template = models.CharField(choices=TEMPLATES, max_length=50, verbose_name='Шаблон')

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('page_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'


class MainImage(models.Model):
    COVER_WIDTH = 1216
    COVER_HEIGHT = 780

    cover = models.ImageField(upload_to='main_slides/%Y/%m/%d/', verbose_name='Изображение')
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Порядок')

    def __str__(self):
        return str(self.id)

    def cover_preview(self):
        cover_url = self.cover.url if self.cover else ''
        return format_html('<img style="max-width: 200px;" src="{0}" alt="" />', cover_url)
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
        ordering = ('order', '-id',)
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения на Главной'
