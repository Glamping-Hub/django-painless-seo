from django.contrib import admin
from django.contrib.contenttypes import generic

from simpleseo.models import SeoMetadata


class SeoMetadataInline(generic.GenericStackedInline):
    model = SeoMetadata
    extra = 1
    max_num = 1


class SeoMetadataAdmin(admin.ModelAdmin):
    list_display = ('path', 'lang_code', )

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ['content_type', 'object_id', 'content_object', ]
        return super(SeoMetadataAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(SeoMetadata, SeoMetadataAdmin)
