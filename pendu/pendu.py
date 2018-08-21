# -*-coding:Latin-1 -*

import utils.fonctions

print("Jeu de pendu, vous avez 8 chances pour trouver le mot")
# Lecture des mots
utils.fonctions.lireListeMots()
motChoisi = utils.fonctions.initialiserPartie()
motTronque= '********'

#Saise nom joueur
utils.fonctions.chargerScores()
utils.fonctions.saisieNomJoueur()

lettreSaisie = str()
saisieOk = False

while lettreSaisie != "q":
    while saisieOk == False:
        lettreSaisie = utils.fonctions.saisieLettre()
        saisieOk = utils.fonctions.controleSaisie(lettreSaisie)

    saisieOk = False
    if len(lettreSaisie) == 0:
        lettreSaisie = 'q'
    else:
        nbTentativesRestantes = utils.fonctions.nbTentativesRestantes()
        motTronque = utils.fonctions.remplacerLettreDansMot(motTronque, motChoisi, lettreSaisie)
        print("Mot découvert {}, nombre de tentatives restantes {}".format(motTronque
                                                                     , nbTentativesRestantes
                                                                     ))
        lettreSaisie = ""

    if lettreSaisie != 'q':
        terminee, typefin = utils.fonctions.partieTerminee(motChoisi, motTronque)
        if terminee:
            if typefin == 1:
                print("Vous n'avez pas trouvé le mot {} en coups".format(motChoisi))
            if typefin == 2:
                print("Bravo vous avez gagné. Votre score est de {}".format(utils.fonctions.recupScore()))
            lettreSaisie = input("Voulez vous rejouer (q pour quitter) ?")

            if lettreSaisie != 'q':
                utils.fonctions.initialiserPartie()

utils.fonctions.sauvegarderScores()