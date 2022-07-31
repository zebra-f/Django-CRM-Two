# settings.py TEMPLATES=[{'OPTIONS': { 'libraries': {'my_tags': 'templatetags.global_tags',}}}] 

from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):

    d = context['request'].GET.copy()

    for key, val in kwargs.items():
        d[key] = val
    for key in [key for key, val in d.items() if not val]:
        del d[key]

    return d.urlencode()