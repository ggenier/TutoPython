# -*- coding: utf-8 -*-

"""Fichier de tests de Roboc"""

from utils.Carte import Carte
import utils.fonctions
import utils.affichage
from Joueur import Joueur

#Test chargement de la liste des cartes
listeCarte=utils.fonctions.getListeCartes("../cartes/*")
print("Liste des cartes dispo :")
print("\t"+str(listeCarte))

#Test création et sauvegarde d'un joueur
joueur = Joueur("ggenier")
#print(str(joueur))
#print("Sauvegarde du joueur")
#utils.fonctions.sauvegarderJoueur("../save/", joueur)

#joueur=None
#print("Chargement du joueur")
#joueur = utils.fonctions.chargerJoueur("ggenier")
#print(str(joueur))

#Test menu sélection carte
#numeroCarte=utils.affichage.affichageListeCarteEtSaisie(listeCarte)
#if str(numeroCarte).isnumeric():
#    print("Carte sélectionnée {} - {}".format(numeroCarte, listeCarte[numeroCarte]))

numeroCarte = 1
#Chargement de la carte, et analyse
carte = Carte(listeCarte[numeroCarte])
carte.analyseCarte()

#On déplace le joueur sur sa position
#TODO a faire si on a chargé un joueur
joueur.setPosition(carte.changerPositionJoueur(None, joueur.getPosition()))

#Affichage de la carte
utils.affichage.affichageStructureCarte(carte.getStructureCarte())

#Test saisie direction
#deplacement = utils.affichage.saisieDeplacement()
deplacement=("n", 1)
print("\nDeplacement vers : "+str(deplacement[0])+"-"+str(deplacement[1]))
joueur.setPosition((0, 2, 3))
nouvellePosition = utils.fonctions.calculerNouvellePosition(joueur.getPosition(), deplacement[0], deplacement[1])
print("Position actuelle {}, nouvelle positon {}".format(joueur.getPosition(), nouvellePosition))
estSortie, nouvellePosition = carte.changerPositionJoueur(joueur.getPosition(), nouvellePosition)
joueur.setPosition(nouvellePosition)
print(str(joueur))

deplacement=("s", 1)
print("\nDeplacement vers : "+str(deplacement[0])+"-"+str(deplacement[1]))
nouvellePosition = utils.fonctions.calculerNouvellePosition(joueur.getPosition(), deplacement[0], deplacement[1])
print("Position actuelle {}, nouvelle positon {}".format(joueur.getPosition(), nouvellePosition))
estSortie, nouvellePosition = carte.changerPositionJoueur(joueur.getPosition(),nouvellePosition)
joueur.setPosition(nouvellePosition)
print(str(joueur))

deplacement=("e", 1)
print("\nDeplacement vers : "+str(deplacement[0])+"-"+str(deplacement[1]))
nouvellePosition = utils.fonctions.calculerNouvellePosition(joueur.getPosition(), deplacement[0], deplacement[1])
print("Position actuelle {}, nouvelle positon {}".format(joueur.getPositionPrecedente(), nouvellePosition))
estSortie, nouvellePosition = carte.changerPositionJoueur(joueur.getPositionPrecedente(), nouvellePosition)
joueur.setPosition(nouvellePosition)
print(str(joueur))

deplacement=("o", 1)
print("\nDeplacement vers : "+str(deplacement[0])+"-"+str(deplacement[1]))
nouvellePosition = utils.fonctions.calculerNouvellePosition(joueur.getPosition(), deplacement[0], deplacement[1])
print("Position actuelle {}, nouvelle positon {}".format(joueur.getPositionPrecedente(), nouvellePosition))
estSortie, nouvellePosition = carte.changerPositionJoueur(joueur.getPositionPrecedente(), nouvellePosition)
joueur.setPosition(nouvellePosition)
print(str(joueur))