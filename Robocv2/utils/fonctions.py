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