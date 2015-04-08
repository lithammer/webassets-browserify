# Browserify filter for webassets [![Build Status](https://travis-ci.org/renstrom/webassets-browserify.svg?branch=master)](https://travis-ci.org/renstrom/webassets-browserify)


Filter for for compiling assets using [Browserify](http://browserify.org) and [webassets](http://webassets.readthedocs.org). Requires Python 2.7 or Python 3.3 and newer.

## Basic usage

```python
from webassets.filter import register_filter
from webassets_browserify import Browserify

register_filter(Browserify)
```

## Usage with Django

This requires [django-assets](http://django-assets.readthedocs.org).

```python
from django_assets import Bundle, register
from webassets.filter import register_filter
from webassets_browserify import Browserify

register_filter(Browserify)

js = Bundle('js/main.js', filters='browserify', output='bundle.js',
            depends='js/**/*.js')
register('js_all', js)
```

## Options

###### BROWSERIFY_BIN

The path to the Browserify binary. If not set, assumes `browserify` is in the system path.

###### BROWSERIFY_TRANSFORMS

A list of Browserify transforms to use. Each transform will be included via Browserify's command-line `--transform` argument.

###### BROWSERIFY_EXTRA_ARGS

A list of any additional command-line arguments. For example:

```python
BROWSERIFY_EXTRA_ARGS = ['--debug', '--ignore', '*.jsx']
```

## License

MIT
