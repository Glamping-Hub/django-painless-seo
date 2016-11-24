# Copyright (C) 2014 Glamping Hub (https://glampinghub.com)
# License: BSD 3-Clause

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

FALLBACK_TITLE = getattr(settings, 'SEO_DEFAULT_TITLE', None)
FALLBACK_DESCRIPTION = getattr(settings, 'SEO_DEFAULT_DESCRIPTION', None)

if FALLBACK_TITLE is None:
    raise ImproperlyConfigured('SEO_DEFAULT_TITLE is not defined in settings.')

if FALLBACK_DESCRIPTION is None:
    raise ImproperlyConfigured('SEO_DEFAULT_DESCRIPTION is not defined in settings.')

I18N = getattr(settings, 'USE_I18N')
DEFAULT_LANG_CODE = getattr(settings, 'LANGUAGE_CODE', 'en')[:2]

if I18N:
    SEO_LANGUAGES = getattr(settings, 'LANGUAGES', None)
    if not SEO_LANGUAGES:
        raise ImproperlyConfigured('If USE_I18N is set to True, you need to define LANGUAGES in settings.')
else:
    SEO_LANGUAGES = ((DEFAULT_LANG_CODE, DEFAULT_LANG_CODE), )

SEO_MODELS = getattr(settings, 'SEO_MODELS', [])
SEO_ADMIN_FORM_REQUIRED_FIELDS = getattr(settings, 'SEO_ADMIN_FORM_REQUIRED_FIELDS', dict())
