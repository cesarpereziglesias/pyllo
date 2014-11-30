import requests
import json

class Entity:

    API_KEY = None
    API_SECRET = None
    API_TOKEN = None

    API_URL = 'https://api.trello.com'
    API_VERSION = '1'

    @staticmethod
    def configure(key, secret, token):
        Entity.API_KEY = key
        Entity.API_SECRET = secret
        Entity.API_TOKEN = token

    @classmethod
    def search(cls, id_):
        url = Entity.get_base_url() + ('%s/%s?key=%s&token=%s' % (cls.__entity__, id_, Entity.API_KEY, Entity.API_TOKEN))

        r = requests.get(url)
        if r.ok:
            return cls(**json.loads(r.text))
        else:
            return null

    @classmethod
    def get_children(cls, id_, cls_child):
        url = Entity.get_base_url() + ('%s/%s/%s?key=%s&token=%s' % (cls.__entity__, id_, cls_child.__entity__, Entity.API_KEY, Entity.API_TOKEN))

        r = requests.get(url)
        children = []
        if r.ok:
            children_response = json.loads(r.text)
            for child in children_response:
                children.append(cls_child(**child))

        return children

    @staticmethod
    def get_base_url():
        return "%s/%s/" % (Entity.API_URL, Entity.API_VERSION)

    def __str__(self):
        return "{0}(id={1},name={2})".format(self.__class__.__name__, self.id, self.name)
