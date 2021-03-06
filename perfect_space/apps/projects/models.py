# coding=utf-8
import os

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.datetime_safe import datetime
from django.utils.html import format_html
from easy_thumbnails.files import get_thumbnailer
from perfect_space.apps.pages.models import SEO


class ProjectAbstract(models.Model):
    COVER_WIDTH = 1327
    COVER_HEIGHT = 710
    THUMB_WIDTH = 355
    THUMB_HEIGHT = 370

    idea_ru = models.TextField(blank=True, verbose_name='Идея')
    content_ru = models.TextField(blank=True, verbose_name='Текст')

    idea_en = models.TextField(blank=True, verbose_name='Идея')
    content_en = models.TextField(blank=True, verbose_name='Текст')

    date_publication = models.DateTimeField(default=datetime.now, verbose_name='Дата публикации', help_text='Сортировка по этому полю')
    slug = models.SlugField(max_length=100, db_index=True, unique=True, verbose_name='Псевдоним')
    cover = models.ImageField(upload_to='projects_cover/%Y/%m/%d/', verbose_name='Обложка')
    thumb = models.ImageField(blank=True, null=True, upload_to='projects_thumb/%Y/%m/%d/', verbose_name='Превью')

    def __str__(self):
        return self.title_ru

    def cover_preview(self):
        cover_url = self.cover.url if self.cover else ''
        return format_html('<img style="max-width: 100%" src="{0}" alt="" />', cover_url)
    cover_preview.short_description = 'Превью'

    def thumb_preview(self):
        thumb_url = self.thumb.url if self.thumb else ''
        return format_html('<img style="max-width: 100%" src="{0}" alt="" />', thumb_url)
    thumb_preview.short_description = 'Превью'

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

    def thumb_resize(self):
        file = self.thumb.file if self.thumb else self.cover.file
        thumb = get_thumbnailer(file, file.name)
        thumb = thumb.get_thumbnail({
            'size': (self.THUMB_WIDTH, self.THUMB_HEIGHT),
            'crop': True
        })
        self.thumb.save(thumb.name, thumb.file, save=False)
        os.remove(thumb.path)

    def save(self, *args, **kwargs):
        self.cover_resize()
        self.thumb_resize()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Project(SEO, ProjectAbstract):
    authors_ru = models.CharField(blank=True, max_length=1024, verbose_name='Авторы')
    address_ru = models.CharField(blank=True, max_length=255, verbose_name='Расположение')
    date_constructed_ru = models.CharField(blank=True, max_length=255, verbose_name='Дата постройки')
    date_planning_ru = models.CharField(blank=True, max_length=255, verbose_name='Проектирование')
    date_realization_ru = models.CharField(blank=True, max_length=255, verbose_name='Реализация')

    authors_en = models.CharField(blank=True, max_length=1024, verbose_name='Авторы')
    address_en = models.CharField(blank=True, max_length=255, verbose_name='Расположение')
    date_constructed_en = models.CharField(blank=True, max_length=255, verbose_name='Дата постройки')
    date_planning_en = models.CharField(blank=True, max_length=255, verbose_name='Проектирование')
    date_realization_en = models.CharField(blank=True, max_length=255, verbose_name='Реализация')

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ('-date_publication',)
