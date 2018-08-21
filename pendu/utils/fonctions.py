# -*- coding: utf-8 -*-

import utils.donnees
import pickle
import random
import codecs

def lireListeMots():
    print("Chargements des mots")
    with codecs.open("utils/listeMots.txt", 'r', encoding='utf-8') as fichierMots:
        utils.donnees.listeMots = fichierMots.read().split(",")

def initialiserPartie():
    motChoisi = utils.fonctions.choisirMot()
    print("*******************************")
    print("Nouvelle patie")
    print("*******************************")
    print("Mot a trouver : " + motChoisi)
    utils.fonctions.nb_coups=0
    return motChoisi

def sauvegarderScores():
    print("Sauvegarde des scores")
    with open("scores", 'wb') as fichierScore:
       objscore = pickle.Pickler(fichierScore)
       objscore.dump(utils.donnees.scores)

def chargerScores():
    print("Chargements des scores")
    with open("scores", 'rb') as fichierScore:
       objpickle = pickle.Unpickler(fichierScore)
       utils.donnees.scores = objpickle.load()

def saisieNomJoueur():
    utils.donnees.nomJoueur=input("Votre nom de joueur : ")
    try:
        print("Votre précédent score est : ", utils.donnees.scores[utils.donnees.nomJoueur])
    except KeyError:
        utils.donnees.scores[utils.donnees.nomJoueur] = 0
        print("Nouveau joueur {}, score {}".format(utils.donnees.nomJoueur, utils.donnees.scores[utils.donnees.nomJoueur]))

def choisirMot():
    numeroRandom = random.randrange(len(utils.donnees.listeMots))
    return str(utils.donnees.listeMots[numeroRandom]).replace("\n", "").strip()

def saisieLettre():
    lettre = input("Saisir une lettre (vide pour quitter) : ")
    return lettre

def remplacerLettreDansMot(motTronque, motChoisi, lettre):
    i = 0
    #print("Taille mot choisi "+str(len(motChoisi)))
    while i < len(motChoisi):
        #print(str(i)+motChoisi[i] +"-"+ lettre)
        if motChoisi[i] == lettre:
            #print(motTronque[0:i])
            #print(str(lettre))
            #print(motTronque[i:len(motTronque)])
            if i == 0:
                motTronque = str(lettre) + motTronque[i+1:len(motTronque)]
            else:
                motTronque = motTronque[0:i] + str(lettre) + motTronque[i + 1:len(motTronque)]

            #print("tt "+motTronque)
        i+=1

    return motTronque

def partieTerminee(motChoisi, motTrouve):
    if nbTentativesRestantes() == -1:
        caculerScore()
        return True, 1
    elif motChoisi == motTrouve:
        caculerScore()
        return True, 2
    else:
        return False, 0

def recupScore():
    #print("Score "+str(utils.donnees.scores[utils.donnees.nomJoueur]))
    return utils.donnees.scores[utils.donnees.nomJoueur]

def caculerScore():
    utils.donnees.scores[utils.donnees.nomJoueur] = utils.donnees.scores[utils.donnees.nomJoueur] + nbTentativesRestantes()
    print("Score calculé : "+str(utils.donnees.scores[utils.donnees.nomJoueur]))

def incrementerCoup():
    utils.donnees.nb_coups+=1
    #print("Nombre coup joué "+str(utils.donnees.nb_coups))

def nbTentativesRestantes():
    tentativesRestantes = utils.donnees.nombre_d_essai - utils.donnees.nb_coups
    print("Nombre de tentatives restantes " + str(tentativesRestantes))
    return tentativesRestantes

def controleSaisie(lettre):
    ok = True
    if len(lettre) != 1 & len(lettre) != 0:
        print("Saisie incorrect. Saisir une lettre")
        ok = False

    if ok & str(lettre).isnumeric():
        print("Saisie incorect. Saisir une lettre")
        ok = False

    incrementerCoup()

    return ok


