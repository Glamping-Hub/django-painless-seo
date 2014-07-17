from setuptools import setup

setup(
    name='Django Simple SEO',
    version='0.0.1',
    author='Glamping Hub',
    author_email='it@glampinghub.com',
    packages=['simpleseo', ],
    url='https://github.com/Glamping-Hub/django-simple-seo',
    license='LICENSE',
    description='Simple SEO tools for Django Framework',
    long_description=open('README.md').read(),
    requires=[
        'Django (>=1.5.0)',
    ],
)
