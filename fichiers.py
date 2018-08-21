# -*-coding:Latin-1 -*

import os

print("R�pertoire courant : "+os.getcwd())

print("Changement de r�pertoire pour c:/tmp")
os.chdir(("c:/tmp"))
print("R�pertoire courant : "+os.getcwd())
print("Cr�ation r�pertoire c:/tmp/gg")
try:
    os.mkdir("gg")
except:
    print("R�pertoire d�j� cr�e")

print("Cr�ation ficher c:/tmp/gg/fichier.txt")
fichier=open("c:/tmp/gg/fichier.txt",  'w')

print("Ecriture dans le ficher c:/tmp/gg/fichier.txt")
fichier.write("Test �criture")

print("Fermeture ficher c:/tmp/gg/fichier.txt")
fichier.close()

print("Overture ficher lecture c:/tmp/gg/fichier.txt")
fichier=open("c:/tmp/gg/fichier.txt",  'r')

print("Lecture dans le ficher c:/tmp/gg/fichier.txt")
ligne = fichier.read()

print("Ligne lue : "+ligne)

print("Fermeture ficher c:/tmp/gg/fichier.txt")
fichier.close()

print("Overture fichier lecture avec with c:/tmp/gg/fichier.txt")
with open("c:/tmp/gg/fichier.txt",  'r') as fichier:
    print("Lecture dans le ficher c:/tmp/gg/fichier.txt")
    ligne = fichier.read()
    print("Ligne lue : "+ligne)

print("Fichier ferm� ?:"+str(fichier.closed))
