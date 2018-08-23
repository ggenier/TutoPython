# -*-coding:Latin-1 -*

""""Executiond de commande système"""

import os

#On ne peut pas capturer l'affichage de la commande, juste son retour
retour=os.system("dir")
print("Resultat commande avec system: "+str(retour))

retour=os.popen("dir")
print("\nResultat commande avec popen: "+str(retour))
print("Ligne lue dans retour : ")
for ligne in retour:
    print("\t"+ligne)
