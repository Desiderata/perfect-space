# coding=utf-8
from django.views.generic import DetailView
from perfect_space.apps.pages.models import Page, MainImage
from perfect_space.apps.publications.models import Publication


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

    def get_context_data(self, **kwargs):
        slug = self.kwargs.get('slug')
        context = super().get_context_data(**kwargs)

        context_method = 'context_' + slug
        if hasattr(self, context_method):
            method = getattr(self, context_method)
            context_addition = method()
            context = dict(context, **context_addition)

        return context

    def context_about(self):
        context = {
            'publications': Publication.objects.all()
        }
        return context

    def context_main(self):
        context = {
            'images': MainImage.objects.all()
        }
        return context
