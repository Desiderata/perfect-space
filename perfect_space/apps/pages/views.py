# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from perfect_space.apps.pages.models import Page


class TemplateMixin:
    template_path = 'pages/'

    def get_template_names(self):
        slug = self.kwargs.get('slug')
        page = get_object_or_404(Page, slug=slug)
        template = "{path}{template}.html".format(path=self.template_path, template=page.template)

        return template


class PageView(TemplateMixin, TemplateView):
    pass

