# -*- coding: utf-8 -*-

"""Fonctions utilitaires"""

import glob
import codecs
import random

global listeCartes
listeCartes=list()
global listeLettreJoueur
listeLettreJoueur=["V", "W", "X", "Y", "Z"]

def getListeCartes(repertoireCarte):
    """Récupère la liste des cartes disponible"""
    listeCartes = glob.glob(repertoireCarte)
    return listeCartes

def chargerCarte(cheminCarte):
    """Charge la carte soit par le chemin donné"""
    planCarte = list()

    print("Chargements de la carte {}".format(cheminCarte))
    with codecs.open(cheminCarte, 'r', encoding='utf-8') as carte:
        for ligne in carte:
            planCarte.append(ligne)

    return planCarte

def choisirLettreJoueur():
    """Choisi une lettre pour le joueur au hasard, et supprime la lettre de la liste pour ne pas la réutiliser"""
    lettre = random.choice(listeLettreJoueur)
    listeLettreJoueur.remove(lettre)
    return lettre

def decomposeMessageDeplacement(deplacementDemande):
    #Structure Xspeudo(0,0,0)
    representation = deplacementDemande[0]
    #On recupère pseudo(0,0,0)
    deplacementDemande = deplacementDemande[1:len(deplacementDemande)]
    #On split sur (
    reste = str(deplacementDemande).split("(")
    pseudo = reste[0]
    position = reste[1][0:len(reste[1])-1]
    position = position.replace("'",'')
    detailPosition = position.split(",")
    etage = detailPosition[0]
    ligne = detailPosition[1]
    colonne = detailPosition[2]
    positions = (etage, ligne, colonne)
    return representation, pseudo, positions

def decomposeMessageObstacle(creationSuppressionObstacle):

    #Structure Xm(0,0,0)
    representation = creationSuppressionObstacle[0]
    direction = creationSuppressionObstacle[1]

    return representation, direction

def actionAEffectuer(message):
    """Decompose le message reçu pour détecter l'action à efefctuer :
    SAI : Sélection de la map
    MAP : Affichage nom de la map
    ADD : Creation du joueur
    DEP : Déplacement
    ACT : Demande de saisie d'une action
    DEB : Début de partie
    MUR : Création d'un mur
    DEL : Suppression d'un mur
    ATT : Attente du début de partie
    INF : Envoi d'un message d'information
    POS : Position du joueur dans le tour
    FIN : Fin de la partie
    QUI : Quitter
    """

    return message[0:3]

def decomposeMessageAction(message):
    """Decompose le reste du message reçu er retourne les données utiles"""

    return message[3:len(message)]