# -*- coding: utf-8 -*-

from .Obstacle import Obstacle

class Sortie(Obstacle):
    """Classe représentant une sortie, non bloquant"""

    def __init__(self):
        Obstacle.__init__(self, "S", False, "U")
