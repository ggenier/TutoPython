# -*- coding: utf-8 -*-

from labyrinthe.Obstacle import Obstacle

"""Classe de gestion du joueur : pseudo, score, positions dans le jeu...
    Le joueur est un obstacle"""

class Joueur(Obstacle):

    def __init__(self, pseudo, representation, socket=None, positionJeu=0):
        """Constructeur du joueur"""
        Obstacle.__init__(self, "J", True, str(representation))
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
        #La réprésentation du joueur sur le plan
        self.representation = representation
        #L'objet que le joueur à remplacer sur la carte. utilisé pour remettre l'élèment après son déplacement
        self.objetPrecedent=None
        self.positionJeu=positionJeu #Position dans le jeu-joueur 1, 2...si 0 la partie n'est pas commencé
        self.nomSocket=socket #Nom de la socket client associée au joueur
        self.aJouer=False #indique si le joueur  a joué ce tour

    def getAJouer(self):
        return self.aJouer

    def setAJouer(self, aJouer):
        self.aJouer = aJouer

    def getSocket(self):
        return self.nomSocket

    def setSocket(self, socket):
        self.nomSocket = socket

    def getPositionJeu(self):
        return self.positionJeu

    def setPositionJeu(self, position):
        self.positionJeu = position

    def getPseudo(self):
        return self.pseudo

    def getObjetPrecedent(self):
        return self.objetPrecedent

    def setObjetPrecedent(self, objetPrecedent):
        self.objetPrecedent = objetPrecedent

    def setPosition(self, position=(0,0,0)):
        """Défini la position du joueur via un tuple(etage, ligne, colonne) et l'objet dont il pris la place"""
        #On se déplace que si on change de position
        if self.position != position:
            self.position = (int(position[0]), int(position[1]), int(position[2]))
            self.histoPosition.append(self.position)

    def setRepresentation(self, representation):
        self.representation = representation

    def getPosition(self):
        """Retourne la position actuelle du joueur"""
        return(self.position[0], self.position[1],self.position[2])

    def getPositionPrecedente(self):
        """Retourne la position précédente du joueur"""
        if len(self.histoPosition)>0:
            return self.histoPosition[len(self.histoPosition)-1]

    def getHisto(self):
        """Retourne le liste des coups joués"""
        return self.histoPosition

    def __str__(self):
        return "Joueur {} ({}), positionné à l'étage {}, ligne {}, colonne {}. Nombre de coups jouées {}.".format(self.pseudo, self.representation, self.position[0], self.position[1]
                                                                                 , self.position[2], len(self.histoPosition))