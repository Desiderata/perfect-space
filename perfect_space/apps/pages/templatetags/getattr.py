# coding=utf-8
from django import template
from django.core.urlresolvers import resolve, reverse
from django.utils import translation
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def getattribute(context, obj, attribute):
    lang = translation.get_language()
    return mark_safe(getattr(obj, '{}_{}'.format(attribute, lang)))


@register.simple_tag(takes_context=True)
def change_lang(context, lang=None, *args, **kwargs):
    """
    Get active page's url by a specified language
    Usage: {% change_lang 'en' %}
    """

    path = context['request'].path
    url = path.replace('/ru/', '/en/') if lang == 'en' else path.replace('/en/', '/ru/')

    return url
