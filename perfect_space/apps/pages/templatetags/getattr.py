# coding=utf-8
from django import template
from django.utils import translation
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def getattribute(context, obj, attribute, length=None, newlines=False):
    lang = translation.get_language()
    name = '{}_{}'.format(attribute, lang)
    content = obj.get(name) if isinstance(obj, dict) else getattr(obj, name)

    if length:
        content = strip_tags(content)[:length]

    if newlines:
        content = content.replace('\n', '<br />')

    return mark_safe(content)


@register.simple_tag(takes_context=True)
def change_lang(context, lang=None, *args, **kwargs):
    """
    Get active page's url by a specified language
    Usage: {% change_lang 'en' %}
    """

    path = context['request'].path
    url = path.replace('/ru/', '/en/') if lang == 'en' else path.replace('/en/', '/ru/')

    return url
