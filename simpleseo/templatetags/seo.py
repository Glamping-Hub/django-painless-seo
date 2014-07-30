from django.template import Library
from django.utils.translation import get_language

from simpleseo import settings
from simpleseo.models import SeoMetadata

register = Library()


@register.filter
def single_quotes(description):
    return description.replace('\"', '\'')


@register.inclusion_tag('simpleseo/metadata.html', takes_context=True)
def get_seo(context):
    lang_code = get_language()[:2]
    path = context['request'].path
    try:
        metadata = SeoMetadata.objects.get(path=path, lang_code=lang_code)
    except SeoMetadata.DoesNotExist:
        metadata = None
    if metadata is None:
        return {'title': settings.FALLBACK_TITLE,
                'description': settings.FALLBACK_DESCRIPTION}
    return {'title': metadata.title, 'description': metadata.description}


@register.simple_tag(takes_context=True)
def get_seo_title(context):
    return get_seo(context)['title']


@register.simple_tag(takes_context=True)
def get_seo_description(context):
    return get_seo(context)['description']
