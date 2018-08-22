# -*- coding: utf-8 -*-

"""Fichier Roboc"""

from utils.Carte import Carte
import utils.fonctions
import utils.affichage
from Joueur import Joueur

repertoireCartes = "cartes/*"
repertoireSauvegardes = "save/"

#Chargement des cartes dispo
listeCarte=utils.fonctions.getListeCartes(repertoireCartes)

#Saisie du pseudo
pseudo = utils.affichage.saisiePseudo()
if len(pseudo) != 0:
    joueur = utils.fonctions.chargerJoueur(repertoireSauvegardes, pseudo)

    if joueur is None:
        joueur = Joueur(pseudo)
    else:
        #La joueur a déjà joué, on l'affiche
        print(joueur)
    quitter = 'n'

    while quitter.lower() != 'q':
       #Sélection de la carte
       numeroCarte=utils.affichage.affichageListeCarteEtSaisie(listeCarte)
       if str(numeroCarte).isnumeric():
          print("Carte sélectionnée {} - {}".format(numeroCarte, listeCarte[numeroCarte]))

          #Chargement de la carte
          carte = Carte(listeCarte[numeroCarte])
          carte.analyseCarte()

          #On déplace le joueur sur sa position, si on est sur la même carte
          if joueur.getCarte() != listeCarte[numeroCarte]:
            #Autre carte, on repart point de départ
            joueur.setPosition((0, 0, 0))
            estSortie, deplacementAutorise, nouvellePosition = carte.changerPositionJoueur(None, joueur.getPosition(), None, None)
          else:
              estSortie, deplacementAutorise, nouvellePosition = carte.changerPositionJoueur(joueur.getPosition(), joueur.getPosition(), None, None)

          joueur.setPosition(nouvellePosition)
          joueur.setCarte(listeCarte[numeroCarte])

          while str(quitter).lower() != 'q':
              # Affichage de la carte
              utils.affichage.affichageStructureCarte(carte.getStructureCarte())

              #Saisie du déplacment
              deplacement = utils.affichage.saisieDeplacement()
              quitter = deplacement[0]

              if str(quitter).lower() != 'q':
                 estSortie, deplacementAutorise, nouvellePosition = carte.changerPositionJoueur(joueur.getPosition(), None, deplacement[0], deplacement[1])
                 if not deplacementAutorise:
                    #On ne sait pas déplacer, le déplacement n'est pas valide
                    utils.affichage.deplacementImpossible()

                 joueur.setPosition(nouvellePosition)

                 #Sauvegarde de la position
                 utils.fonctions.sauvegarderJoueur(repertoireSauvegardes, joueur)

              if estSortie == True:
                  #Dernier affichage de la carte
                  utils.affichage.affichageStructureCarte(carte.getStructureCarte())
                  #Fin du jeu
                  print("Félicitations ! Vous avez gagné !")
                  rejouer='q'
                  while rejouer.lower() != 'n' and rejouer.lower() != 'o':
                      rejouer=input("Voulez-vous rejouer (o)ui, (n)on, ou (v)oir vos vous joués ?")
                      if str(rejouer).lower() == 'v':
                          utils.affichage.afficherHisto(joueur.getHisto())

                  if str(rejouer).lower() == 'n':
                      quitter='q'

                  #Partie finie, on reinitialise le joueur
                  joueur.reinitJoueur()
                  #Sauvegarde de la position
                  utils.fonctions.sauvegarderJoueur(repertoireSauvegardes, joueur)
                  break

