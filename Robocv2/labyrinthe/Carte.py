# -*- coding: utf-8 -*-

import utils.fonctions
from .Mur import Mur
from .Sortie import Sortie
from .Porte import Porte
from .Obstacle import Obstacle
import random

class Carte:
    """Classe permettant la gestion des cartes :
    - chargement
    - sauvegarde"""

    def __init__(self, cheminCarte=None):
        self.cheminCarte = cheminCarte
        self.structureCarte=dict()
        self.structureCarteInitiale = dict()
        self.caracterePrecedent=" "
        self.nbColonneMax = 0
        self.nbLigneMax = 0

    def getCheminCarte(self):
        return self.cheminCarte

    def analyseCarte(self, cheminCarte=None):
        """Analyse la carte pour la mettre dans un dictionnaire pour le jeu, soi par le chemin donné
        soit celui donné par le constructeur

        La structure du labyrinthe est représentée par un tuple de la position et l'objet représenté

        """

        if cheminCarte is not None:
            self.cheminCarte = cheminCarte
        planCarte = utils.fonctions.chargerCarte(self.cheminCarte)

        print("Analyse carte")
        #On parcourt la carte
        #Le schema du dico sera base sur un tuble :
        # - l'étage, la ligne, la colonne = objet correspondant
        etage=0
        ligne=0
        colonne=0
        for lignePlan in planCarte:
            for lettre in lignePlan:
                objetCree = self.creationObjet(lettre)
                objetCree.setPosition((etage, ligne, colonne))
                self.structureCarte[etage, ligne, colonne] = objetCree
                objetCreeIni = self.creationObjet(lettre)
                self.structureCarteInitiale[etage, ligne, colonne] = objetCreeIni
                colonne+=1

            ligne+=1
            self.nbColonneMax = colonne - 1
            colonne=0

        self.nbLigneMax = ligne - 1



    def getStructureCarte(self):
        """Retourne le dico de la carte"""
        return self.structureCarte

    def setStructureCarte(self, structureCarte):
        """Ecrase la structure de la carte"""
        self.structureCarte = structureCarte

    def creationObjet(self, lettre):
        """Création de l'obet en focntion de son type dans le fichier carte"""

        objetCree = None

        if lettre.lower() == "o":
            objetCree = Mur()

        if lettre.lower() == ".":
            objetCree = Porte()

        if lettre.lower() == "u":
            objetCree = Sortie()

        #Un vide
        if objetCree is None:
            objetCree = Obstacle("V", False, " ")

        return objetCree

    def rechercheEmplacementLibre(self):
        """Recherche un emplacement libre
        Retourne True si on a trouvé un emplacement vide, et les positions étage, ligne, colonne
        """

        trouve = True
        #Construction de la liste des emplacements libres
        listeEmplacementLibre=list()
        for position in self.structureCarte:
            etage = position[0]
            ligne = position[1]
            colonne = position[2]
            obstacle = self.structureCarte[position[0], position[1], position[2]]
            #Si on est sur un emplacement libre ou une porte, et pas une sortie
            if not obstacle.getBloquant() and not isinstance(obstacle, Sortie) and colonne < self.nbColonneMax and ligne < self.nbLigneMax:
                listeEmplacementLibre.append(position)

        #Aucun emplacement de libre
        if len(listeEmplacementLibre) == 0:
            trouve = False
            etage=None
            ligne=None
            colonne=None
        else:
            #On tire au hasard un emplacement libre
            elementTire = random.choice(listeEmplacementLibre)
            etage = elementTire[0]
            ligne = elementTire[1]
            colonne = elementTire[2]

        return trouve, etage, ligne, colonne

    def deplacementAutorise(self, position, direction, nbDeplacements):
        """Controle que le déplacement est autorisé, on va pas dans un mur, il n'y a pas de joueur..."""
        etage = position[0]
        ligne = position[1]
        colonne = position[2]

        deplacementCourant = 0
        deplacementAutorise = True
        sortie = False
        positionsPrecedentes = position

        while deplacementCourant < nbDeplacements:
            #Calcul de la nouvelle position
            if direction.lower() == "n":
                ligne-=1

            if direction.lower() == "s":
                ligne+=1

            if direction.lower() == "e":
                colonne+=1

            if direction.lower() == "o":
                colonne-=1

            obstacle = self.structureCarte[etage, ligne, colonne]
            if obstacle.getBloquant():
                deplacementAutorise = False
                break

            #On est sur une sortie
            if isinstance(obstacle, Sortie):
                sortie = True
                break

            positionsPrecedentes = obstacle.getPosition()
            deplacementCourant+=1

        #Si le déplacement n'a pas été autorisé, on renvoit le déplacement le plus loin
        if not deplacementAutorise and not sortie:
            (etage, ligne, colonne) = positionsPrecedentes

        return deplacementAutorise, sortie, etage, ligne, colonne


    def getObstacle(self, position=(0,0,0)):
        """Retourne l'objet aux positions demandées"""
        return self.structureCarte[position]

    def setObstacle(self, obstacle=None, type=None, positions=(0,0,0)):
        """Crée l'objet demandé aux positions indiquées sans calcul
        ou on positionne directement l'objet"""
        if obstacle is not None:
            self.structureCarte[obstacle.getPosition()] = obstacle
        else:
            objetCree = self.creationObjet(type)
            objetCree.setPosition(positions)
            self.structureCarte[positions] = objetCree
            #On va forcer la structure initiale pour avoir le bon symbol à l'affichage
            self.structureCarteInitiale[positions] = objetCree

    def creationObstacle(self, type, direction, positions=(0,0,0)):
        """Creation d'un obstacle du type indiqué aux positions indiquées
        Cette fonction calcul les nouvelles coordonnées de l'obstacle
        On retourne  les nouvelles positions pour mettre à jour les clients
        """
        objetCree = self.creationObjet(type)
        creationPossible = True

        #Calcul des positions de l'obstacle
        etage = positions[0]
        ligne= positions[1]
        colonne= positions[2]
        if direction.lower() == "n":
            ligne -= 1

        if direction.lower() == "s":
            ligne += 1

        if direction.lower() == "e":
            colonne += 1

        if direction.lower() == "o":
            colonne -= 1

        objetInitial = self.structureCarte[(etage, ligne, colonne)]
        #On ne peut pas mettre un mur ou une porte sur la sortie ou sur u joueur
        if isinstance(objetInitial, Sortie) or objetInitial.getType().lower() == "j":
            creationPossible = False
        else:
            #Ajout de l'objet à la carte
            self.structureCarte[(etage, ligne, colonne)] = objetCree

        return creationPossible, (etage, ligne, colonne)

    def positionnerJoueur(self, joueur):
        """Positionne le joueur à son emplacement"""
        self.structureCarte[joueur.getPosition()] = joueur

    def viderStructure(self):
        for position in self.structureCarte:
            etage = position[0]
            ligne = position[1]
            colonne = position[2]
            obstacle = self.structureCarte[position[0], position[1], position[2]]
            obstacleInitial = self.structureCarteInitiale[position[0], position[1], position[2]]

            #Si on est sur un joueur ou une porte, on remet l'ojet original, sinon on laisse ce qui a été crée
            if obstacle.getType() == "J":
                self.structureCarte[position[0], position[1], position[2]] = Obstacle("V", False, " ")
                if obstacleInitial.getType() == "P":
                    self.structureCarte[position[0], position[1], position[2]] = Porte()

