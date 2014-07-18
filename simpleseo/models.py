from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _

from simpleseo import settings


class SeoMetadata(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    title = models.CharField(verbose_name=_('Title'), max_length=68)
    description = models.CharField(verbose_name=_('Description'), max_length=155)
    path = models.CharField(verbose_name=_('Path'), max_length=200, db_index=True,
                            help_text=_("This should be an absolute path, excluding the domain name. Example: '/foo/bar/'."))
    lang_code = models.CharField(verbose_name=_('Language'), max_length=2, choices=settings.SEO_LANGUAGES)

    class Meta:
        verbose_name = _('SEO metadata')
        verbose_name_plural = _('SEO metadata')
        db_table = 'seo_metadata'
        unique_together = (('path', 'lang_code'), )
        ordering = ('path', 'lang_code')

    def __unicode__(self):
        return "SEO Metadata for %s" % (self.path)
