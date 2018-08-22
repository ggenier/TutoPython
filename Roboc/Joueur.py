# -*- coding: utf-8 -*-

"""Classe de gestion du joueur : pseudo, score, positions dans le jeu..."""

class Joueur():
    def __init__(self, pseudo):
        """Constructeur du joueur"""
        #Pseudo
        self.pseudo = pseudo
        #Score
        self.score = 0
        #Historique des coups joués
        self.histoPosition = list()
        # La position du joueur est repésenté par le tuple avec l'étage, ligne, et colonne
        self.position = (0, 0, 0)
        #Position précedente dans la carte
        self.positionPrecedente = (0, 0, 0)
        #Carte en cours de jeu
        self.carte=str()

    def setCarte(self, carte):
        self.carte = carte

    def getCarte(self):
        return self.carte

    def getPseudo(self):
        return self.pseudo

    def setPosition(self, position=(0,0,0)):
        """Défini la position du joueur via un tuple(etage, ligne, colonne)"""
        #On se déplace que si on change de position
        if self.position != position:
            self.position = position
            self.histoPosition.append(self.position)

    def getPosition(self):
        """Retourne la position actuelle du joueur"""
        return self.position

    def getPositionPrecedente(self):
        """Retourne la position précédente du joueur"""
        if len(self.histoPosition)>0:
            return self.histoPosition[len(self.histoPosition)-1]

    def reinitJoueur(self):
        self.score = 0
        #Historique des coups joués
        self.histoPosition = list()
        # La position du joueur est repésenté par le tuple avec l'étage, ligne, et colonne
        self.position = (0, 0, 0)
        self.positionPrecedente = (0, 0, 0)
        self.carte = str()

    def getHisto(self):
        """Retourne le liste des coups joués"""
        return self.histoPosition

    def __str__(self):
        return "Joueur {}, positionné à l'étage {}, ligne {}, colonne {}. Nombre de coups jouées {}".format(self.pseudo, self.position[0], self.position[1]
                                                                                 , self.position[2], len(self.histoPosition))