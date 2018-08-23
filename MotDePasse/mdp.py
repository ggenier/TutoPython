# -*-coding:Latin-1 -*

"""Gestion des mots de passe

Utiliser le terminal python de l'IDE ou de l'os"""

import getpass
import hashlib

#Saisi du premier mot de passe
motPasse=getpass.getpass("Saisir votre mot de passe : ")
print("Vous avez saisi {}".format(motPasse))

print("\nChiffrement du mot de passe")
mdpChiffr=hashlib.sha3_512(motPasse.encode())
print(mdpChiffr)
print("Mdp chiffré : "+mdpChiffr.hexdigest())

#Saisi du deuxième mot de passe
motPasse=getpass.getpass("\nSaisir un mot de passe : ")
print("Vous avez saisi {}".format(motPasse))
print("\nChiffrement du mot de passe")
mdpChiffr_2=hashlib.sha3_512(motPasse.encode())
print(mdpChiffr)
print("Mdp chiffré : "+mdpChiffr_2.hexdigest())

#Conrole s'ils sont identiques
print("\nLes deux mots de passe sont identique {} ".format(mdpChiffr.hexdigest()==mdpChiffr_2.hexdigest()))