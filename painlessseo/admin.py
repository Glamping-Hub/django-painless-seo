# Copyright (C) 2014 Glamping Hub (https://glampinghub.com)
# License: BSD 3-Clause

from django import forms
from django.contrib import admin
from django.utils.translation import ugettext as _
import django

try:
    from django.contrib.contenttypes.admin import GenericStackedInline
except:
    from django.contrib.contenttypes.generic import GenericStackedInline

from django.utils.safestring import mark_safe

from . import settings
from .models import SeoMetadata, register_seo_signals


def get_language(obj):
    language = dict(settings.SEO_LANGUAGES).get(obj.lang_code, obj.lang_code)
    return mark_safe('<strong>%s</strong>' % language.upper())


class SEOMetadataWithValidationForm(forms.ModelForm):

    def validate_required_fields(self, cleaned_data, fields):
        error_msg = _(u'This field is required')
        for field in fields:
            value = cleaned_data.get(field)
            if not value:
                if django.VERSION >= (1, 7):
                    self.add_error(field, error_msg)
                else:
                    self._errors[field] = self.error_class([error_msg])
                    del cleaned_data[field]
        return cleaned_data

    def clean(self):
        cleaned_data = super(SEOMetadataWithValidationForm, self).clean()
        obj = cleaned_data.get('id')
        for lang, fields in settings.SEO_ADMIN_FORM_REQUIRED_FIELDS.items():
            if obj.lang_code == lang:
                cleaned_data = self.validate_required_fields(cleaned_data,
                                                             fields)
        return cleaned_data


class SeoMetadataInline(GenericStackedInline):
    exclude = ('path', 'lang_code', )
    extra = 0
    max_num = 0
    model = SeoMetadata

    fields = ('language', 'site', 'title', 'description')
    readonly_fields = ('language', 'site', )

    def has_delete_permission(self, request, obj=None):
        return False

    def language(self, obj):
        return get_language(obj)
    language.short_description = 'Language'


class SeoMetadataWithValidationInline(SeoMetadataInline):
    form = SEOMetadataWithValidationForm


class SeoMetadataAdmin(admin.ModelAdmin):
    list_display = ('path', 'lang_code', 'site', )
    search_fields = ['path', ]
    list_filter = ('lang_code', 'site', )
    exclude = ('content_type', 'object_id', )

    fields = ('language', 'site', 'title', 'description', )
    readonly_fields = ('language', 'site', )

    def language(self, obj):
        return get_language(obj)
    language.short_description = 'Language'


admin.site.register(SeoMetadata, SeoMetadataAdmin)
register_seo_signals()
