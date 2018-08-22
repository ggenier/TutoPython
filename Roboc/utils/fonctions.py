# -*- coding: utf-8 -*-

"""Fonctions utilitaires"""

import glob
import pickle
import os

global listeCartes
listeCartes=list()

def getListeCartes(repertoireCarte):
    """Récupère la liste des cartes disponible"""
    listeCartes = glob.glob(repertoireCarte)
    return listeCartes

def creationRepertoireSauvegarde(repertoireSauvegarde):
    """Création du répertoire s'il n'existe pas"""
    repertoireACreer=str()
    listeRepertoire = repertoireSauvegarde.split("/")
    for repertoire in listeRepertoire:
        if str(repertoire) != "/":
            repertoireACreer += "/"+repertoire
            if os.path.exists(os.getcwd()+"/"+repertoireACreer) == False:
                os.mkdir(os.getcwd()+"/"+repertoireACreer)

def sauvegarderJoueur(repertoireSauvegarde, joueur):
    """Sauvegarde des donnees du joueur"""
    #print("Sauvegarde des donnes du joueur")
    repertoireSauvegarde += "/"+joueur.getPseudo()
    creationRepertoireSauvegarde(repertoireSauvegarde)
    with open(os.getcwd()+"/"+repertoireSauvegarde+"/save.player", 'wb') as fichierJoueur:
       objscore = pickle.Pickler(fichierJoueur)
       objscore.dump(joueur)


def chargerJoueur(repertoireSauvegarde, nomJoueur=None):
    """Chargement du joueur
    Retourne le joueur chargé
    NOTE : Pour l'instant gestion d'un unique joueur
    Il faudra supprimer le None dans le paramètre
    """
    #print("Chargements du joueur {}".format(nomJoueur))
    repertoireSauvegarde+="/"+nomJoueur+"/"
    creationRepertoireSauvegarde(repertoireSauvegarde)
    joueur=None
    try:
        with open(os.getcwd()+"/"+repertoireSauvegarde+"/save.player", 'rb') as fichierJoueur:
           objpickle = pickle.Unpickler(fichierJoueur)
           joueur = objpickle.load()
    except FileNotFoundError:
        #Le fichier n'existe pas, on ne fait rien
        print("Nouveau joueur")
        pass

    return joueur

def calculerNouvellePosition(positionJoueur, direction, nbDeplacement):
    """Fonction de calcul de la nouvelle position du joueur sous la forme de tuple
    etage, ligne, colonne
    La fonction ne déplce pas le joueur
    La fonction ne controle pas la validité du déplacement dans le plan
    Elle teste uniquement pour ne pas passer sous les -1 au nord ou a l'ouest.
    """
    etage = positionJoueur[0]
    ligne = positionJoueur[1]
    colonne = positionJoueur[2]

    if str(direction).lower() == 'n':
        ligne-=int(nbDeplacement)
        if ligne < 0:
            ligne = 0

    if str(direction).lower() == 's':
        ligne+=int(nbDeplacement)

    if str(direction).lower() == 'e':
        colonne+=int(nbDeplacement)

    if str(direction).lower() == 'o':
        colonne-=int(nbDeplacement)
        if colonne < 0:
            colonne = 0

    return (etage, ligne, colonne)
