# Django PainlessSEO

[![Code Climate](https://codeclimate.com/github/Glamping-Hub/django-painless-seo/badges/gpa.svg)](https://codeclimate.com/github/Glamping-Hub/django-painless-seo)

A painless way to add SEO information to your Django site.

## Features

This app provides two ways of adding SEO metadata to your django site:

- Absolute paths
- Model instances

It's fully integrated with the admin site including inline forms for models.
It also includes support for multiple languages and localized URLs, and having
several sites.

## Requirements

    Django >= 1.5.0

## Installation

The Git repository can be cloned with this command:

    git clone https://github.com/Glamping-Hub/django-painless-seo.git

The `painlessseo` package included in the distribution should be placed on the
`PYTHONPATH`. Add `painlessseo` to the `INSTALLED_APPS` in your *settings.py*.
Run `syncdb` command to create the needed tables.

## Settings

PainlessSEO uses two configuration variables in order to define the default
information that will be displayed if the URL has no SEO metadata related. You
have to add them to your *settings.py*:

    SEO_DEFAULT_TITLE = 'Lorem ipsum title'
    SEO_DEFAULT_DESCRIPTION = 'Lorem ipsum description'

### Registering Models

To create synced SEO metadata for model instances you have to define the
`SEO_MODELS` variable in your *settings.py* like this:

    SEO_MODELS = (
        ('myapp', 'mymodel'),
        ('anotherapp', 'anothermodel'),
    )

After registering the models, you can add the inline form to the admin instance
for each model:

    from painlessseo.admin import SeoMetadataInline

    class MyModelAdmin(admin.ModelAdmin):
        inlines = [SeoMetadataInline, ]

Now every time you save a model instance through the admin site, the SEO
metadata will be updated automatically.

## SEO Output

As simple as loading the `seo` template library and using the `get_seo`
template tag like this:

    {% load seo %}

    <head>
        {% get_seo %}
    </head>

## Notes

[Why PainlessSEO does not include keywords meta tag](http://googlewebmastercentral.blogspot.in/2009/09/google-does-not-use-keywords-meta-tag.html).

## Legal Stuff

This software is licensed under the terms of the BSD 3-clause license. You can
find the whole text of the license in the LICENSE file.
