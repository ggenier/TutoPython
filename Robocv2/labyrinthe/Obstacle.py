# -*- coding: utf-8 -*-

class Obstacle():
    """Classe représentant un élèment du labyrnthe boquant ou pas"""

    def __init__(self, type=None, bloquant=None, representation=None, position=None):
        """Type de l'obstacle : mur, porte, escalier..."""
        self.type=type
        #Est ce que l'obstacle est bloquant ?
        self.bloquant=bloquant
        #Comment est représenté cet élèment à l'écran
        self.representation=representation
        #Position de l'objet
        self.position=position

    def getType(self):
        return self.type

    def getBloquant(self):
        return self.bloquant

    def getRepresentation(self):
        return self.representation

    def setPosition(self, position):
        self.position = position

    def getPosition(self):
        return self.position

    def __str__(self):
        return "(Obstacle : type {}, bloquant {}, representation {}, position {})".format(self.type, self.bloquant, self.representation, self.position)