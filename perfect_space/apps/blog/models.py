# coding=utf-8
import os

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.html import format_html
from easy_thumbnails.files import get_thumbnailer
from math import ceil, floor

from perfect_space.apps.pages.models import SEO


class Tag(models.Model):
    name_ru = models.CharField(max_length=255, verbose_name='Имя')
    name_en = models.CharField(max_length=255, verbose_name='Имя')

    @classmethod
    def regroup(cls, tags):
        columns = 3
        total = tags.count()
        part = ceil(total / columns)
        stop = part
        tags_list = []
        column = 1

        for i, tag in enumerate(tags, 1):
            tags_list.append({
                'id': tag.id,
                'name_ru': tag.name_ru,
                'name_en': tag.name_en,
                'column': column,
            })

            if stop <= i < total:
                part = ceil((total - stop) / (columns - column))
                stop = i + part
                column += 1

        return tags_list

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(SEO):
    COVER_WIDTH = 1327
    COVER_HEIGHT = 710
    THUMB_WIDTH = 205
    THUMB_HEIGHT = 205

    summary_ru = models.TextField(blank=True, max_length=200, verbose_name='Краткое описание', help_text='Выводится на странице блога (список постов)')
    summary_en = models.TextField(blank=True, max_length=200, verbose_name='Краткое описание', help_text='Выводится на странице блога (список постов)')

    annotation_ru = models.CharField(blank=True, max_length=1024, verbose_name='Аннотация')
    content_ru = models.TextField(blank=True, verbose_name='Текст')

    annotation_en = models.CharField(blank=True, max_length=1024, verbose_name='Аннотация')
    content_en = models.TextField(blank=True, verbose_name='Текст')

    date_publication = models.DateTimeField(verbose_name='Дата публикации', help_text='Сортировка по этому полю')
    slug = models.SlugField(max_length=100, db_index=True, unique=True, verbose_name='Псевдоним')
    cover = models.ImageField(upload_to='projects_cover/%Y/%m/%d/', verbose_name='Обложка')
    thumb = models.ImageField(blank=True, null=True, upload_to='projects_thumb/%Y/%m/%d/', verbose_name='Превью')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

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

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ('-date_publication', )
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
