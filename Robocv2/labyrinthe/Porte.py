# -*- coding: utf-8 -*-

from .Obstacle import Obstacle

class Porte(Obstacle):
    """Classe représentant une porte, non bloquant"""

    def __init__(self):
        Obstacle.__init__(self, "P", False, ".")
