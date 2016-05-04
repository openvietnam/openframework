# from openframework.v1.wsgi import Controller


class BasicController(object):

    # Define support for GET on a collection
    def index(self, req):
        data = {
            'action': "index",
            'controller': "basic"
        }
        return data

    def delete(self, req, id):
        data = {
            'action': "delete",
            'controller': "basic",
            'id': id
        }
        return data

    def update(self, req, id):
        data = {
            'action': "update",
            'controller': "basic",
            'id': id
        }
        return data

    def create(self, req):
        data = {
            'action': "create",
            'controller': "basic"
        }
        return data

    def show(self, req, id):
        data = {
            'action': "show",
            'controller': "basic",
            'id': id
        }
        return data


    def detail(self, req):
        data = {
            'action': 'detail',
            'controller': 'basic',
        }
        return data

    def mem_action(self, req, id):
        data = {
            'action': 'mem_action',
            'controller': 'basic',
            'id': id
        }
        return data


class Basics:
    collection_name = 'basics'
    member_name = 'basic'
    controller = BasicController()
    parent_resource = {}
    collection = {'detail': 'GET'}
    member = {'mem_action': 'GET'}