from openframework import wsgi
# import routes.Mapper
from routes import Mapper

from .resource_extensions.basic import Basics

class APIRouterV1(wsgi.Router):
    """

    """

    def __init__(self):
        mapper = Mapper()
        resource = Basics()
        mapper.resource(resource.member_name,
                        resource.collection_name,
                        controller=wsgi.Resource(resource.controller),
                        member=resource.member,
                        collection=resource.collection)

        super(APIRouterV1, self).__init__(mapper)

    @classmethod
    def factory(cls, global_config, **local_conf):
        return cls()