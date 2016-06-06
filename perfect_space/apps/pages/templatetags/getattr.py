# coding=utf-8
from django import template
from django.utils import translation
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def getattribute(context, obj, attribute):
    lang = translation.get_language()
    return mark_safe(getattr(obj, '{}_{}'.format(attribute, lang)))
