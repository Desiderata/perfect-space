# coding=utf-8
from django import template

register = template.Library()


class PageNode:
    def __init__(self, num, is_current=False):
        """
        :type num: str &hellip or page number
        :type is_current: bool
        """
        self.num = num
        self.is_current = is_current


@register.inclusion_tag('pagination.html')
def pagination(request, paginator, page_obj):
    """
    :param objects: Page
    :return:
    """
    show_only_one = False
    pages_before = 1
    pages_after = 1
    pages_show_first = 2
    pages_show_last = 2
    pages_total = paginator.num_pages
    page_current = page_obj.number
    pages = []

    if pages_total == 1 and not show_only_one:
        return

    skip = False
    for p in paginator.page_range:
        is_current = page_current == p
        if pages_show_first < p <= pages_total - pages_show_last \
                and (p < page_current - pages_before or p > page_current + pages_after):
            if skip:
                continue

            page = PageNode(0, is_current)
            pages.append(page)
            skip = True
        else:
            page = PageNode(p, p == page_current)
            pages.append(page)
            skip = False

    return {
        'request': request,
        'previous_page_number': page_obj.previous_page_number() if page_obj.has_previous() else None,
        'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
        'pages': pages,
    }


@register.simple_tag(takes_context=True)
def url_replace(context, field, value):
    dict_ = context['request'].GET.copy()
    dict_[field] = value
    return dict_.urlencode()
