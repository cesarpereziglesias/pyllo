# -*- coding: utf-8 -*-
import requests

from . import Entity

class Card(Entity):

    __entity__ = 'cards'

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', "").encode('utf-8')

    def add_comment(self, comment):
        url = Entity.get_base_url() + ('cards/%s/actions/comments?key=%s&token=%s' % (self.id, Entity.API_KEY, Entity.API_TOKEN))
        requests.post(url, data={"text": comment})

    def move_to_list(self, list_id):
        url = Entity.get_base_url() + ('cards/%s/idList?key=%s&token=%s' % (self.id, Entity.API_KEY, Entity.API_TOKEN))
        requests.put(url, data={"value": list_id})
