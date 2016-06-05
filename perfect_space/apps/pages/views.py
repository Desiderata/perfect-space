# coding=utf-8
from django.views.generic import DetailView
from perfect_space.apps.pages.models import Page


class TemplateMixin:
    template_path = 'pages/'

    def get_template_names(self):
        template = "{path}{template}.html".format(path=self.template_path, template=self.object.template)
        return template


class PageView(TemplateMixin, DetailView):
    model = Page
    context_object_name = 'page'

    def get_object(self, queryset=None):
        return super().get_object(queryset)
