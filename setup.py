from setuptools import setup

setup(
    name='Django SimpleSEO',
    version='0.0.1',
    author='Glamping Hub',
    author_email='it@glampinghub.com',
    packages=['simpleseo'],
    url='https://github.com/Glamping-Hub/django-simple-seo',
    license='LICENSE',
    description='Simple SEO app for django framework',
    long_description=open('README.md').read(),
    requires=[
        'Django (>=1.5.0)',
    ],
)
