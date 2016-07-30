# coding=utf-8
from django.core.urlresolvers import reverse
from django.db import models
from perfect_space.apps.pages.models import SEO
from perfect_space.apps.projects.models import ProjectAbstract


class Interior(SEO, ProjectAbstract):
    square = models.CharField(blank=True, max_length=255, verbose_name='Площадь')
    ceil = models.CharField(blank=True, max_length=255, verbose_name='Высота потолков')
    bedrooms = models.PositiveSmallIntegerField(blank=True, verbose_name='Спален')

    def get_absolute_url(self):
        return reverse('interior_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Интерьер'
        verbose_name_plural = 'Интерьеры'
        ordering = ('-date_publication',)
