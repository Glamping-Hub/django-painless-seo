# Copyright (C) 2014 Glamping Hub (https://glampinghub.com)
# License: BSD 3-Clause

from setuptools import setup

setup(
    name='django-painless-seo',
    version='0.0.3',
    author='Glamping Hub',
    author_email='it@glampinghub.com',
    packages=['painlessseo'],
    url='https://github.com/Glamping-Hub/django-painless-seo',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
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
