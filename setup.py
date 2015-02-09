from setuptools import setup

setup(
    name='django-simple-seo',
    version='0.0.1',
    author='Glamping Hub',
    author_email='it@glampinghub.com',
    packages=['simpleseo'],
    url='https://github.com/Glamping-Hub/django-simple-seo',
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
    description='Simple SEO app for Django framework',
    keywords='seo django',
    long_description=open('README.md').read(),
    requires=[
        'Django (>=1.5.0)',
    ],
)
