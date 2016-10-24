# Copyright (C) 2014 Glamping Hub (https://glampinghub.com)
# License: BSD 3-Clause

from django.contrib import admin

try:
    from django.contrib.contenttypes.admin import GenericStackedInline
except:
    from django.contrib.contenttypes.generic import GenericStackedInline

from django.utils.safestring import mark_safe

from . import settings
from .models import SeoMetadata, register_seo_signals


def get_language_name(lang_code):
    return dict(settings.SEO_LANGUAGES).get(lang_code, lang_code)


class SeoMetadataInline(GenericStackedInline):
    model = SeoMetadata
    extra = 0
    max_num = 0
    exclude = ('path', 'lang_code', )

    fields = ('language', 'title', 'description')
    readonly_fields = ('language', )

    def has_delete_permission(self, request, obj=None):
        return False

    def language(self, obj):
        language = get_language_name(obj.lang_code)
        return mark_safe('<strong>%s</strong>' % language.upper())
    language.short_description = 'Language'


class SeoMetadataAdmin(admin.ModelAdmin):
    list_display = ('path', 'lang_code', )
    search_fields = ['path', ]
    list_filter = ('lang_code', )
    exclude = ('content_type', 'object_id', )

    fields = ('language', 'title', 'description')
    readonly_fields = ('language', )

    def language(self, obj):
        language = get_language_name(obj.lang_code)
        return mark_safe('<strong>%s</strong>' % language.upper())
    language.short_description = 'Language'


admin.site.register(SeoMetadata, SeoMetadataAdmin)
register_seo_signals()
