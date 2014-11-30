# -*- coding: utf-8 -*-
from entity import Entity
from card import Card
from list import List
from board import Board

def configure(key, secret, token):
    Entity.API_KEY = key
    Entity.API_SECRET = secret
    Entity.API_TOKEN = token

__all__ = ["Entity", "Card", "List", "Board"]
