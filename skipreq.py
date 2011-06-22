from nose.plugins.errorclass import ErrorClass, ErrorClassPlugin

from gdata.client import RequestError


class SkipRequestError(ErrorClassPlugin):
    """
    Plugin that will skip tests that raise Google's ``gdata.client.RequestError``.
    When RequestError is raised, the exception will be logged in the skipped
    attribute of the result, 'S' or 'SKIP' (verbose) will be output, and
    the exception will not be counted as an error or failure. This plugin
    is disabled by default but may be enabled with the ``--skipreq`` option.
    """
    enabled = False
    skipped = ErrorClass(RequestError,
                         label='SKIP',
                         isfailure=False)

    def options(self, parser, env):
        """
        Add my options to command line.
        """
        env_opt = 'NOSE_WITH_SKIP_REQ'
        parser.add_option('--skip-req', action='store_true',
                          dest='skipreq', default=env.get(env_opt, False),
                          help="Enable special handling of RequestError "
                          "exceptions.")

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

