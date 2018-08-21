# -*-coding:Latin-1 -*

from DictionnaireOrdonne import DictionnaireOrdonne

#dico = DictionnaireOrdonne()
#print(str(dico))

print("Test dico2")
dico2 = DictionnaireOrdonne(tomate=12, pomme=13)
print(str(dico2))

print("\nNb pommes {} ".format((dico2['pomme'])))
dico2['tomate']=24
print("Nouveau nb de tomates {} ".format(dico2['tomate']))

print("\nSuppression tomate")
del dico2['tomate']
print(str(dico2))

print("\nAjout abricot")
dico2['abricot']=36
print(str(dico2))

print("\nRecherche valeur poire {}".format('poire' in dico2))
print("Recherche valeur pomme {}".format('pomme' in dico2))

print ("\nTaille du dictionnaire {}".format(len(dico2)))

print("\nListe des clés")
for cle in dico2.keys():
    print("\t"+cle)

print("\nListe des valeurs")
for valeur in dico2.values():
    print("\t{}".format(valeur))

print("\nListe des items")
for item in dico2.items():
    print("\t{} {}".format(item[0], item[1]))

print("\nAjout de dico2+dico2bis")
dico2bis=DictionnaireOrdonne(poire=50, fraise=65, pomme=26)
print(dico2bis)
dico2=dico2+dico2bis
print("Nouveau dico2")
print(dico2)

print("\nTri de dico2 (sort)")
dico2.sort()
print(dico2)

print("\nTri de dico2 (reverse)")
dico2.reverse()
print(dico2)

#dico 3 et 4 ne fonctionne pas pour l'instant
#print("Test dico3")
#dico3 = DictionnaireOrdonne(dico2)
#print(str(dico3))

#dico4 = dict(radis=10, courgette=25)
#dico5 = DictionnaireOrdonne(dico4)
#print(str(dico5))