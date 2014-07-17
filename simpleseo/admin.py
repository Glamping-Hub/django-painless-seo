from django.contrib import admin
from django.contrib.contenttypes import generic

from simpleseo.models import SeoMetadata


class SeoMetadataInline(generic.GenericStackedInline):
    model = SeoMetadata
    extra = 1


class SeoMetadataAdmin(admin.ModelAdmin):
    list_display = ('path', 'lang_code', )


admin.site.register(SeoMetadata, SeoMetadataAdmin)
