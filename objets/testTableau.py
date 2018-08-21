# -*-coding:Latin-1 -*

from objets.Personne import Personne
from objets.TableauNoir import TableauNoir

#moi = Personne("GENIER", "GREGOIRE", 36, "TOURS")
#print("{} {} {} {}".format(moi.nom, moi.prenom, moi.age, moi.adresse))

tableau = TableauNoir()
tableau.ecrire("Test 1")
tableau.ecrire("Test 2")

print("Etat tableau :\n")
print(tableau.lire())

tableau.effacer()
print("Etat tableau après effacement :\n")
print(tableau.lire())

tableau2 = TableauNoir()
tableau.combienTableaux()
tableau2.combienTableaux()

tableau3 = TableauNoir()
print(tableau3.surface)
tableau3.surface = "Test 3"
print(tableau3.surface)

print("\nInfos objet :")
tableau3

chaine=str(tableau3)
print(chaine)