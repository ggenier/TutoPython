# -*- coding: utf-8 -*-

from .Obstacle import Obstacle

class Mur(Obstacle):
    """Classe représentant un mur, boquant"""

    def __init__(self):
        Obstacle.__init__(self, "M", True, "O")
