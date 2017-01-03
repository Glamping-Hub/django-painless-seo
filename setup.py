# Copyright (C) 2014 Glamping Hub (https://glampinghub.com)
# License: BSD 3-Clause

import fnmatch
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


def recursive_include(directory, patterns):
    result = []
    for root, dirs, files in os.walk(directory):
        child_root = root.replace(directory, '').lstrip('/')
        for pattern in patterns:
            result.extend([os.path.join(child_root, name)
                           for name in fnmatch.filter(files, pattern)])
    return result


setup(
    name='django-painless-seo',
    version='0.2.0',
    author='Glamping Hub',
    author_email='it@glampinghub.com',
    packages=find_packages('.'),
    include_package_data=True,
    package_data={
        '': recursive_include('painlessseo', [
            '*.html', '*.css', '*.js', '*.txt', '*.png', '*.ico', '*.wsgi',
            '*.xml', '*.gif', '*.jpg', '*.otf', '*.svg', '*.example', '*.woff',
            '*.md',
        ])
    },
    url='https://github.com/Glamping-Hub/django-painless-seo',
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet'
    ],
    description='Painless SEO app for Django framework',
    keywords='seo django',
    long_description=open('README.md').read(),
    requires=[
        'Django (>=1.5.0)',
    ],
)
