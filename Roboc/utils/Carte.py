# -*- coding: utf-8 -*-

import pickle
import codecs

class Carte:
    """Classe permettant la gestion des cartes :
    - chargement
    - sauvegarde"""

    def __init__(self, cheminCarte):
        self.cheminCarte = cheminCarte
        self.planCarte = list()
        self.structureCarte=dict()
        self.caracterePrecedent=" "
        self.nbColonneMax = 0
        self.nbLigneMax = 0

    def chargeCarte(self, cheminCarte=None):
        """Charge la carte soit par le chemin donné, soit par celui donnée au constructeur"""
        if cheminCarte is not None:
            self.cheminCarte = cheminCarte
            self.planCarte = list()
            self.structureCarte = dict()

        print("Chargements de la carte {}".format(self.cheminCarte))
        with codecs.open(self.cheminCarte, 'r', encoding='utf-8') as carte:
            for ligne in carte:
                self.planCarte.append(ligne)

    def analyseCarte(self, cheminCarte=None):
        """Analyse la carte pour la mettre dans un dictionnaire pour le jeu, soi par le chemin donné
        soit celui donné par le constructeur"""
        self.chargeCarte(cheminCarte)

        print("Analyse carte")
        #On parcourt la carte
        #Le schema du dico sera base sur un tuble :
        # - l'étage, la ligne, la colonne = lettre
        etage=0
        ligne=0
        colonne=0
        for lignePlan in self.planCarte:
            for lettre in lignePlan:
                self.structureCarte[etage, ligne, colonne] = lettre
                colonne+=1

            self.nbLigneMax = ligne
            ligne+=1
            self.nbColonneMax = colonne
            colonne=0

        self.nbColonneMax-=1
        self.nbLigneMax -= 1

    def getNbLigneMax(self):
        return self.nbLigneMax

    def getNbColonneMax(self):
        return self.nbColonneMax

    def changerPositionJoueur(self, anciennePosition, nouvellePosition, direction, nbDeplacement):
        """Déplace le joueur d'ancienne position vers nouvelle positions
        Si anciennePosition=None on cherche la position par défaut"""

        estSortie = False
        deplacementAutorise = False  # Par défaut
        caractereFuturPosition=" "

        if anciennePosition is not None:
            if anciennePosition[0] == 0 and anciennePosition[1] == 0 and anciennePosition[1] == 0 :
                anciennePosition = None

        #Recherche de la position de départ dans le fichier
        if anciennePosition is None:
            for position in self.structureCarte:
                if self.structureCarte[position[0], position[1], position[2]] == 'X':
                    anciennePosition = (position[0], position[1], position[2])
                    nouvellePosition = anciennePosition
                    #On a trouvé, pas la peine de continuer
                    break
        else:
            #On recherche le point de départ pour reprendre où on c'est arrêté
            if anciennePosition == nouvellePosition and direction is None and nbDeplacement is None:
                for position in self.structureCarte:
                    if self.structureCarte[position[0], position[1], position[2]] == 'X':
                        nouvellePosition = anciennePosition
                        anciennePosition = (position[0], position[1], position[2])
                        if str(self.structureCarte[nouvellePosition]).lower() != 'x':
                            self.caracterePrecedent = self.structureCarte[nouvellePosition]
                        else:
                            self.structureCarte[nouvellePosition] = " "
                        deplacementAutorise = True  # Par défaut
                        #On a trouvé, pas la peine de continuer
                        break

        #Mise en place de la nouvelle position
        if anciennePosition is not None:
            #On controle si on a aucun mur sur le chemin
            if direction is not None and nbDeplacement is not None:
                i=1
                while i <= int(nbDeplacement):
                    #Déplacement vers le haut
                    if str(direction).lower() == "n":
                        ligneActuelle =  anciennePosition[1] - i
                        if ligneActuelle > 0:
                            nouvellePosition = (anciennePosition[0], anciennePosition[1]-i, anciennePosition[2])
                            caractereFuturPosition = self.structureCarte[nouvellePosition]
                            estSortie = self.estSortie(caractereFuturPosition)
                            if estSortie == True:
                                #Pas la peine de continuer
                                deplacementAutorise = True
                                break
                            if self.deplacementAutorise(caractereFuturPosition):
                                deplacementAutorise = True
                            else:
                                deplacementAutorise = False
                        else:
                            deplacementAutorise = False

                    if str(direction).lower() == "s":
                        ligneActuelle =  anciennePosition[1]+i
                        if ligneActuelle < self.nbLigneMax:
                             nouvellePosition = (anciennePosition[0], anciennePosition[1]+i, anciennePosition[2])
                             caractereFuturPosition = self.structureCarte[nouvellePosition]
                             estSortie = self.estSortie(caractereFuturPosition)
                             if estSortie == True:
                                 # Pas la peine de continuer
                                 deplacementAutorise = True
                                 break
                             if self.deplacementAutorise(caractereFuturPosition):
                                deplacementAutorise = True
                             else:
                                deplacementAutorise = False
                        else:
                            deplacementAutorise = False

                    if str(direction).lower() == "e":
                        colonneActuelle =  anciennePosition[2]+i
                        if colonneActuelle < self.nbColonneMax:
                            nouvellePosition = (anciennePosition[0], anciennePosition[1], anciennePosition[2]+i)
                            caractereFuturPosition = self.structureCarte[nouvellePosition]
                            estSortie = self.estSortie(caractereFuturPosition)
                            if estSortie == True:
                                #Pas la peine de continuer
                                deplacementAutorise = True
                                break
                            if self.deplacementAutorise(caractereFuturPosition):
                                deplacementAutorise = True
                            else:
                                deplacementAutorise = False
                        else:
                            deplacementAutorise = False

                        print(deplacementAutorise)

                    if str(direction).lower() == "o":
                        colonneActuelle =  anciennePosition[2]-i
                        if colonneActuelle > 0:
                            nouvellePosition = (anciennePosition[0], anciennePosition[1], anciennePosition[2]-i)
                            caractereFuturPosition = self.structureCarte[nouvellePosition]
                            estSortie = self.estSortie(caractereFuturPosition)
                            if estSortie == True:
                                #Pas la peine de continuer
                                deplacementAutorise = True
                                break
                            if self.deplacementAutorise(caractereFuturPosition):
                                deplacementAutorise = True
                            else:
                                deplacementAutorise = False
                        else:
                            deplacementAutorise = False

                    #Pas la peine d'aller plus loin
                    if not deplacementAutorise:
                        nouvellePosition = anciennePosition
                        break

                    i+=1

            if deplacementAutorise:
                if direction is not None and nbDeplacement is not None:
                    # Déplacement autorisé et pas le début de partie
                    self.structureCarte[anciennePosition[0], anciennePosition[1], anciennePosition[2]] = self.caracterePrecedent
                    self.structureCarte[nouvellePosition[0], nouvellePosition[1], nouvellePosition[2]] = "X"
                    # on sauvegarde le caractere pour le remettre après, si ce n'est pas le joueur
                    if str(caractereFuturPosition).lower() != "x":
                        self.caracterePrecedent = caractereFuturPosition
                else:
                    #Début de partie
                    self.structureCarte[anciennePosition[0], anciennePosition[1], anciennePosition[2]] = " "
                    self.structureCarte[nouvellePosition[0], nouvellePosition[1], nouvellePosition[2]] = "X"

        #On retourne la position du joueur, utile notamment pourle début de partie
        return estSortie, nouvellePosition


    def deplacementAutorise(self, caractereFuturPosition):
        """Contrôle si le déplacement est autorisé, pas dans un mur"""
        deplacementAutorise=True
        if str(caractereFuturPosition).lower() == 'o':
            deplacementAutorise = False

        return deplacementAutorise

    def estSortie(self, caractereFuturPosition):
        """Retourne True si on est sur le sortie"""
        estSortie = False
        if str(caractereFuturPosition).lower() == "u":
            estSortie = True

        return estSortie

    def getStructureCarte(self):
        """Retourne le dico de la carte"""
        return self.structureCarte
