from nose.plugins import Plugin
from nose.plugins.skip import SkipTest

from gdata.client import RequestError


class SkipRequestError(Plugin):
    """
    Plugin that will skip tests that raise Google's ``gdata.client.RequestError``.
    When RequestError is raised, the exception will be logged in the skipped
    attribute of the result, 'S' or 'SKIP' (verbose) will be output, and
    the exception will not be counted as an error or failure. This plugin
    is disabled by default but may be enabled with the ``--skipreq`` option.
    """
    codes = None
    enable = False

    def options(self, parser, env):
        """
        Add my options to command line.
        """
        env_opt = 'NOSE_WITH_SKIP_REQ'
        parser.add_option('--skip-req', action='store_true',
                          dest='skipreq', default=env.get(env_opt, False),
                          help="Enable special handling of RequestError "
                          "exceptions.")
        parser.add_option('--skip-req-codes', action='store',
                          dest='skipreq_codes', default='',
                          help="Comma-separated list of status codes to"
                          "ignore.")

    def configure(self, options, conf):
        """
        Configure plugin. Skip plugin is enabled by default.
        """
        if not self.can_configure:
            return
        self.conf = conf
        enable = getattr(options, 'skipreq', False)
        if enable:
            self.enabled = True
        codes = getattr(options, 'skipreq_codes', None)
        if codes:
            self.codes = [int(c) for c in codes.split(',')]

    def formatError(self, test, err):
        ec, ev, et = err
        ei = test.exc_info()[1]
        if ec == RequestError and (not self.codes or
                                   ei.status
                                   in self.codes):
            return (SkipTest, err[1], err[2])
        return err

