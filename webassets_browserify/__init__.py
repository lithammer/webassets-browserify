from webassets.filter import ExternalTool, option

__all__ = ['Browserify']


class Browserify(ExternalTool):
    """Use Browserify to bundle assets.

    Requires the Browserify executable to be available externally. You can
    install it using `Node Package Manager <http://npmjs.org/>`_::

        $ npm install -g browserify

    Supported configuration options:

    BROWSERIFY_BIN
        The path to the Browserify binary. If not set, assumes ``browserify``
        is in the system path.

    BROWSERIFY_TRANSFORMS
        A list of Browserify transforms to use. Each transform will be included
        via Browserify's command-line ``--transform`` argument. If you need
        to pass arguments to a transform, use a list:
        ``['babelify', '--stage', '0']``

    BROWSERIFY_EXTRA_ARGS
        A list of any additional command-line arguments.

    """

    name = 'browserify'
    max_debug_level = None
    method = 'output'
    options = {
        'binary': 'BROWSERIFY_BIN',
        'transforms': option('BROWSERIFY_TRANSFORMS', type=list),
        'extra_args': option('BROWSERIFY_EXTRA_ARGS', type=list)
    }

    def setup(self):
        super(Browserify, self).setup()
        self.argv = [self.binary or 'browserify']

        for transform in self.transforms or []:
            if isinstance(transform, (list, tuple)):
                self.argv.extend(('--transform', '['))
                self.argv.extend(transform)
                self.argv.append(']')
            else:
                self.argv.extend(('--transform', transform))

        if self.extra_args:
            self.argv.extend(self.extra_args)

    def input(self, infile, outfile, **kwargs):
        self.argv.append(kwargs['source_path'])

    def output(self, infile, outfile, **kwargs):
        self.subprocess(self.argv, outfile, infile)
