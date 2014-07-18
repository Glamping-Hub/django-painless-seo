from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

FALLBACK_TITLE = getattr(settings, 'SEO_DEFAULT_TITLE', None)
FALLBACK_DESCRIPTION = getattr(settings, 'SEO_DEFAULT_DESCRIPTION', None)

if FALLBACK_TITLE is None:
    raise ImproperlyConfigured('SEO_DEFAULT_TITLE is not defined in settings.')

if FALLBACK_DESCRIPTION is None:
    raise ImproperlyConfigured('SEO_DEFAULT_DESCRIPTION is not defined in settings.')

SEO_LANGUAGES = getattr(settings, 'LANGUAGES', None)
