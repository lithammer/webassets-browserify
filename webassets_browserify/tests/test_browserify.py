from unittest import TestCase

from webassets.filter import register_filter
from webassets.test import TempEnvironmentHelper

from webassets_browserify import Browserify


register_filter(Browserify)


class BrowserifyFilterTestCase(TempEnvironmentHelper, TestCase):

    default_files = {
        'main.js': 'var foo = 1;'
    }

    def setUp(self):
        super(BrowserifyFilterTestCase, self).setup()

    def test_browserify_filter(self):
        self.mkbundle('main.js', filters='browserify',
                      output='bundle.js').build()
        assert 'var foo = 1;' in self.get('bundle.js')
