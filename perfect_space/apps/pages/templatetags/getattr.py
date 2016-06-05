# coding=utf-8
from django import template
from django.utils import translation

register = template.Library()


@register.simple_tag(takes_context=True)
def getattribute(context, obj, attribute):
    lang = translation.get_language_from_request(context.request)
    return getattr(obj, '{}_{}'.format(attribute, lang))
