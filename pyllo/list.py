# -*- coding: utf-8 -*-
from . import Entity

class List(Entity):

    __entity__ = 'lists'

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', "").encode('utf-8')
