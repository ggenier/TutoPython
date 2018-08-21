# -*-coding:Latin-1 -*

import random
import math

#Retourne comment le joueur a gagn�
def typeGain(numeroChoisi, couleurChoisie, numeroRandom, couleurRandom):
    if numeroChoisi == numeroRandom:
        return "numero"

    resteChoisi = numeroChoisi % 2
    resteRandom = numeroRandom % 2
    if (couleurChoisie == couleurRandom) & ((resteChoisi == 0 & resteRandom == 0) | (resteChoisi != 0 & resteRandom != 0)):
        return "couleur"

def montantGain(typeGain, sommeMisee):
    gain = 0
    if typeGain == "numero":
        gain = sommeMisee*3

    if typeGain == "couleur":
        gain = math.ceil((sommeMisee*50)/100)

    return gain

print("Bienvenue au ZCasino, vous jouez � la roulette")

abandon = False
while abandon != True:
    numeroChoisi = input("Saisir votre num�ro (0-49) (a)bandon pour quitter: ")
    if numeroChoisi.upper() == "A":
        abandon = True
    else:
        try:
            numeroChoisi = int(numeroChoisi)
        except:
            print("Num�ro invalide")
            continue

        #Test si num�ro valide 0-50
        if numeroChoisi<0 & numeroChoisi>49:
            print("Le num�ro doit �tre compris entre 0 et 49")
            continue

    while abandon != True:
        #Couleur
        couleurChoisie = input("Quelle couleur (Noir (n)/Rouge(r)/(a)bandon) : ")
        if couleurChoisie.upper() != "A":
            if couleurChoisie.upper() != 'N' and couleurChoisie.upper() != "R":
                print("La couleur doit �tre (n)oir ou (r)ouge ou (a)bandon pour quitter)")
                continue
            else:
                break

    #Montant mise
    while abandon != True:
        montantMise = input("Saisir le montant mis� en $ (a)bandon pour quitter : ")
        if montantMise.upper() == "A":
            abandon = True
        else:
            try:
                montantMise = int(montantMise)
            except:
                print("Montant invalide")
                continue

        #Saisie OK
        numeroRandom = random.randrange(50)
        couleurRandom = random.randrange(1) #0 noir, 1 blanc
        if couleurRandom == 0:
            couleurRandom = "n"
        else:
            couleurRandom = "r"

        typeGain=typeGain(numeroChoisi, couleurChoisie, numeroRandom, couleurRandom)
        gain=montantGain(typeGain, montantMise)

        if gain != 0:
            print("Vous avez gagn� ", gain, "$, sur \"", typeGain,"\"")
            print("Num�ro Random : ", numeroRandom)
            print("Couleur Random : ", couleurRandom)
        else:
            print("Vous avez perdu")
        break
