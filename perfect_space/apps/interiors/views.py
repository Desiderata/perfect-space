# coding=utf-8
from django.utils.datetime_safe import datetime
from django.views.generic import DetailView, ListView
from perfect_space.apps.interiors.models import Interior
from perfect_space.apps.pages.models import Page


class InteriorDetail(DetailView):
    model = Interior
    context_object_name = 'page'
    template_name = 'interiors/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['interiors_similar'] = Interior.objects.exclude(pk=self.object.pk)[:3]
        return context


class InteriorList(ListView):
    model = Interior
    context_object_name = 'interiors'
    template_name = 'interiors/list.html'
    slug = 'interiors'

    def get_queryset(self):
        return self.model.objects.filter(date_publication__lte=datetime.now())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = Page.objects.get(slug=self.slug)
        return context
