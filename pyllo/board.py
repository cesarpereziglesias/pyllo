# -*- coding: utf-8 -*-
from . import Entity, Card, List

class Board(Entity):

    __entity__ = 'boards'

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', "").encode('utf-8')

    def get_cards(self):
        return Board.get_children(self.id, Card)

    def get_lists(self):
        return Board.get_children(self.id, List)
