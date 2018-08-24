# -*-coding:Latin-1 -*

import unittest
from labyrinthe.Carte import Carte
import utils.affichage
import utils.fonctions
from Joueur import Joueur


def deplacerJoueur(joueur, direction, deplacement):
    deplacementAutorise, etage, ligne, colonne = carte.deplacementAutorise(joueur.getPosition(), direction, nbDeplacement)
    if deplacementAutorise:
        #On positionne le joueur à sa nouvelle position
        joueur.setPosition((etage, ligne, colonne))
        #On sauvegarde l'ancien objet si non nul
        NouvelObstacle = carte.getObstacle(joueur.getPosition())
        #On récupère l'ancien objet du joueur
        obstacleARemettre = joueur.getObjetPrecedent()
        joueur.setObjetPrecedent(NouvelObstacle)
        carte.setObstacle(obstacleARemettre)
        carte.positionnerJoueur(joueur)
        utils.affichage.affichageStructureCarte(structureCarte)

carte = Carte("maps/facile.txt")
carte.analyseCarte()

joueur = Joueur("ggenier", utils.fonctions.choisirLettreJoueur())
structureCarte = carte.getStructureCarte()
#utils.affichage.affichageStructureCarte(structureCarte)
trouve, etage, ligne, colonne = carte.rechercheEmplacementLibre()


if trouve:
    #Debut de partie, on déplace le joueur
    joueur.setPosition((etage, ligne, colonne))
    NouvelObstacle = carte.getObstacle(joueur.getPosition())
    obstacleARemettre = joueur.getObjetPrecedent()
    joueur.setObjetPrecedent(NouvelObstacle)
    carte.positionnerJoueur(joueur)
    utils.affichage.affichageStructureCarte(structureCarte)

    #On joue sur une porte
    #COntrole que le déplacement est autorisé
    deplacementAutorise, etage, ligne, colonne = carte.deplacementAutorise(joueur.getPosition(), "s", 20)
    if deplacementAutorise:
        joueur.setPosition((etage, ligne, colonne))
        #On sauvegarde l'ancien objet si non nul
        NouvelObstacle = carte.getObstacle(joueur.getPosition())
        #On récupère l'ancien objet du joueur
        obstacleARemettre = joueur.getObjetPrecedent()
        joueur.setObjetPrecedent(NouvelObstacle)
        carte.setObstacle(obstacleARemettre)
        carte.positionnerJoueur(joueur)
        utils.affichage.affichageStructureCarte(structureCarte)

    #On joue sur une porte
    #COntrole que le déplacement est autorisé
    deplacementAutorise, etage, ligne, colonne = carte.deplacementAutorise(joueur.getPosition(), "o", 20)
    if deplacementAutorise:
        joueur.setPosition((etage, ligne, colonne))
        #On sauvegarde l'ancien objet si non nul
        NouvelObstacle = carte.getObstacle(joueur.getPosition())
        #On récupère l'ancien objet du joueur
        obstacleARemettre = joueur.getObjetPrecedent()
        joueur.setObjetPrecedent(NouvelObstacle)
        carte.setObstacle(obstacleARemettre)
        carte.positionnerJoueur(joueur)
        utils.affichage.affichageStructureCarte(structureCarte)
