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
        via Browserify's command-line ``--transform`` argument.

    BROWSERIFY_EXTRA_ARGS
        A list of any additional command-line arguments.

    """

    name = 'browserify'
    max_debug_level = None
    options = {
        'binary': 'BROWSERIFY_BIN',
        'transforms': option('BROWSERIFY_TRANSFORMS', type=list),
        'extra_args': option('BROWSERIFY_EXTRA_ARGS', type=list)
    }

    def input(self, infile, outfile, **kwargs):
        args = [self.binary or 'browserify']

        for transform in self.transforms or []:
            args.extend(('--transform', transform))

        if self.extra_args:
            args.extend(self.extra_args)

        args.append(kwargs['source_path'])

        self.subprocess(args, outfile, infile)
