# -*- coding: utf-8 -*-
"""
Browserify filter for webassets
--------------------

Filter for for compiling assets using Browserify[1] and webassets[2].

Basic usage
`````

.. code:: python

    from webassets.filter import register_filter
    from webassets_browserify import Browserify

    register_filter(Browserify)


Usage with Django
`````

This requires django-assets[3].

.. code:: python

    from django_assets import Bundle, register
    from webassets.filter import register_filter
    from webassets_browserify import Browserify

    register_filter(Browserify)

    js = Bundle('js/main.js', filters='browserify', output='bundle.js',
                depends='js/**/*.js')
    register('js_all', js)


Links
`````

[1] http://browserify.org
[2] http://webassets.readthedocs.org
[3] http://django-assets.readthedocs.org

"""
from setuptools import setup, find_packages


setup(name='webassets_browserify',
      version='1.0.0',
      description='Browserify filter for webassets',
      long_description=__doc__,
      author='Peter Renström',
      license='MIT',
      url='https://github.com/renstrom/webassets-browserify',
      packages=find_packages(),
      keywords=['browserify', 'webassets', 'django assets'],
      install_requires=['webassets'],
      test_suite='tests',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4'
      ])
