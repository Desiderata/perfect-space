# coding=utf-8
from itertools import chain
from operator import attrgetter

from django.db.models import Q
from django.views.generic import ListView

from perfect_space.apps.blog.models import Post
from perfect_space.apps.interiors.models import Interior
from perfect_space.apps.pages.models import Page
from perfect_space.apps.projects.models import Project


class SearchList(ListView):
    context_object_name = 'results'
    template_name = 'search/list.html'
    slug = 'search'
    paginate_by = 20

    def get_queryset(self):
        query = self.request.GET.get('q')
        projects = Project.objects.filter(Q(content_ru__contains=query) | Q(content_en__contains=query))
        interiors = Interior.objects.filter(Q(content_ru__contains=query) | Q(content_en__contains=query))
        posts = Post.objects.filter(Q(content_ru__contains=query) | Q(content_en__contains=query))
        results = sorted(
            chain(projects, interiors, posts),
            key=attrgetter('date_publication'),
        )
        return results

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = Page.objects.get(slug=self.slug)
        context['q'] = self.request.GET.get('q')
        return context
