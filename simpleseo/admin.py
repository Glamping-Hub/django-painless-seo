from django.contrib import admin

from simpleseo.models import SeoMetadata


class SeoMetadataAdmin(admin.ModelAdmin):
    list_display = ('path', 'lang_code', )


admin.site.register(SeoMetadata, SeoMetadataAdmin)
