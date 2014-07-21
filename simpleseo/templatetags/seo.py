from django.template import Library

from simpleseo import settings
from simpleseo.models import SeoMetadata

register = Library()


@register.filter
def single_quotes(description):
    return description.replace('\"', '\'')


@register.inclusion_tag('simpleseo/metadata.html', takes_context=True)
def get_seo(context):
    request = context['request']
    lang_code = request.LANGUAGE_CODE
    path = request.path
    try:
        metadata = SeoMetadata.objects.get(path=path, lang_code=lang_code)
    except SeoMetadata.DoesNotExist:
        metadata = None
    if metadata is None:
        return {'title': settings.FALLBACK_TITLE, 'description': settings.FALLBACK_DESCRIPTION}
    return {'title': metadata.title, 'description': metadata.description}
