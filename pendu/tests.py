# -*-coding:Latin-1 -*

import utils.fonctions

#Saise nom joueur
motTronque = "********"
motChoisi = "azertyui"
lettre='a'
motTronque = utils.fonctions.remplacerLettreDansMot(motTronque, motChoisi, lettre)
print("motTronque "+motTronque)

lettre='z'
motTronque = utils.fonctions.remplacerLettreDansMot(motTronque, motChoisi, lettre)
print("motTronque "+motTronque)

lettre='e'
motTronque = utils.fonctions.remplacerLettreDansMot(motTronque, motChoisi, lettre)
print("motTronque "+motTronque)

lettre='u'
motTronque = utils.fonctions.remplacerLettreDansMot(motTronque, motChoisi, lettre)
print("motTronque "+motTronque)
