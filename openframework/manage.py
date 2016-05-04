from webob import Response
from webob.dec import wsgify


class ShowVersion(object):
    """
    Show version application.
    """

    def __init__(self, version):
        self._version = version

    @wsgify
    def __call__(self, request):
        template = """<h1>Open Framework <h1>
            <h2>Version: <h2>
            <div>{}<div>
            """.format(self._version)
        return Response(template)


    @classmethod
    def factory(cls, global_conf, **local_conf):
        return cls(local_conf['version'])