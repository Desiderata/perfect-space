# coding=utf-8
from collections import OrderedDict

from django.views.generic import ListView, DetailView
from perfect_space.apps.blog.models import Post, Tag
from perfect_space.apps.pages.models import Page


class BlogDetail(DetailView):
    model = Post
    context_object_name = 'page'
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts_similar'] = Post.objects.all()[:3]
        return context


class BlogList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/list.html'
    slug = 'blog'

    def get_queryset(self):
        tag = self.request.GET.get('tag')
        query = Post.objects.filter(tags__id__in=[tag]) if tag else Post.objects.all()

        return query

    def get_context_data(self, **kwargs):
        tag_id = self.request.GET.get('tag')
        context = super().get_context_data(**kwargs)
        context['page'] = Page.objects.get(slug=self.slug)
        context['tag'] = Tag.objects.get(pk=tag_id) if tag_id else None
        return context


class BlogTags(ListView):
    model = Tag
    context_object_name = 'tags'
    template_name = 'blog/tags.html'
    slug = 'blog_tags'

    def get_queryset(self):
        lang = self.request.LANGUAGE_CODE
        tags_query = Tag.objects.order_by('name_{}'.format(lang))
        tags = Tag.regroup(tags_query)
        return tags

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = Page.objects.get(slug=self.slug)
        return context
