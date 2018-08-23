# -*- coding: utf-8 -*-

"""Fonctions de gestion de l'affichage, menu, carte, saisie choix..."""

def saisiePseudo():
    """Saisie du pseudo"""
    pseudo = input("Saisir votre pseudo vide pour quitter) : ")
    return pseudo

def deplacementImpossible():
    """"Indique que le déplacement n'est pas possible"""
    print("Déplacement demandé impossible")

def afficherHisto(histo):
    """Affiche l'historique des coups joués"""
    rang=0
    for coups in histo:
        #On saute le coup de départ
        if rang != 0:
            print("Coups joué n°{} : {} {} {}".format(rang, coups[0], coups[1], coups[2]))
        rang+=1

def affichageListeCarteEtSaisie(listeCarte):
    """Affiche la liste des cartes dans un menu, et demande la sélection du joueur.
    Param : Liste des cartes
    Retour Le choix"""
    print("Labyrinthes existants :")
    touche=1 #Touche à saisir dans le menu
    for carte in listeCarte:
        carteTemp = str(carte).split("\\")
        carteTemp = carteTemp[1].replace(".txt","")
        carte = carteTemp
        print("\t {} - {}.".format(touche, carte))
        touche+=1

    retour=str()
    choix=str()
    saisieValide=False
    #Tant qu'on pas saisie Q ou si on a saisie un alpha, on reste
    while (str(choix).upper() != 'Q') and not saisieValide:
        choix=input("Entrez un numéro de labyrinthe pour commencer à jouer (Q pour quitter) : ")
        #Si on a saisie un choix
        if str(choix).isnumeric():
            if int(choix) == 0 or (int(choix) > int(touche)):
                #Choix non valide
                saisieValide = False
            else:
                #On a bien sélectionné une carte valide
                choix = int(choix) - 1
                retour = listeCarte[choix]
                saisieValide = True
        else:
            #On souhaite quitter
            retour = choix
            saisieValide = False

    return choix

def affichageStructureCarte(structureCarte):
    """Affiche la structure du plan"""
    lignePlan=str()
    prevLigne=0

    for position in structureCarte:
        etage = position[0]
        ligne = position[1]
        colonne = position[2]
        caractere = structureCarte[position[0], position[1], position[2]]

        if prevLigne == ligne:
            lignePlan += caractere
        else:
            print(lignePlan.strip())
            lignePlan=str()
            lignePlan += caractere

        prevLigne = ligne

    #Affichage de la dernière ligne
    print(lignePlan.strip())

def saisieDeplacement():
    """Saisie du déplacement a effectué"""

    saisieValide = False
    deplacement=""
    direction=""
    nombreDeplacement=1

    while deplacement.upper() != 'Q' and not saisieValide:
        deplacement = input("> ")
        #Le déplacement doit cmmencer par une direction
        if deplacement.startswith(("n", "s", "e", "o")):
            direction = deplacement[0]
            if len(deplacement) > 1:
                nombreDeplacement = deplacement[1:len(deplacement)]
                if not nombreDeplacement.isnumeric():
                    print(
                        "Le déplacement doit commencer par une direction : (n)ord, (s)ud, (e)st, (o)est, ou (Q)uitter.\n Il est possible d'ajouter un nombre de déplacement (facultatif)")
                    saisieValide = False
                else:
                    saisieValide = True
            else:
                saisieValide = True
        else:
            if deplacement.isalpha() and deplacement.upper() == 'Q':
                saisieValide = False
                direction = 'Q'
            else:
                print(
                    "Le déplacement doit commencer par une direction : (n)ord, (s)ud, (e)st, (o)est, ou (Q)uitter.\n Il est possible d'ajouter un nombre de déplacement (facultatif)")

    return (direction, nombreDeplacement)