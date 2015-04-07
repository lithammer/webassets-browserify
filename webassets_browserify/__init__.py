from webassets.filter import ExternalTool, option

__all__ = ['Browserify']


class Browserify(ExternalTool):

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
