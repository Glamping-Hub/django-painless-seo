# Copyright (C) 2014 Glamping Hub (https://glampinghub.com)
# License: BSD 3-Clause

from django.forms.models import model_to_dict
from django.template import Library
from django.utils.translation import get_language

from .. import settings
from ..models import SeoMetadata

register = Library()


@register.filter
def single_quotes(description):
    return description.replace('\"', '\'')


@register.inclusion_tag('painlessseo/metadata.html', takes_context=True)
def get_seo(context, **kwargs):
    path = context['request'].path
    lang_code = get_language()[:2]
    try:
        metadata = model_to_dict(SeoMetadata.objects.get(path=path,
                                                         lang_code=lang_code))
    except SeoMetadata.DoesNotExist:
        metadata = {}
    result = {}
    for item in ['title', 'description']:
        result[item] = (metadata.get(item) or
                        kwargs.get(item) or
                        getattr(settings, 'FALLBACK_{0}'.format(item.upper())))
    return result


@register.simple_tag(takes_context=True)
def get_seo_title(context, default=''):
    return get_seo(context, title=default).get('title')


@register.simple_tag(takes_context=True)
def get_seo_description(context, default=''):
    return get_seo(context, description=default).get('description')
