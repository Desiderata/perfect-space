# coding=utf-8
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify


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
