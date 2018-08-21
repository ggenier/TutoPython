# -*-coding:Latin-1 -*

inventaire = dict()
inventaire["pommes"] = 22
inventaire["melons"] = 4
inventaire["poires"] = 18
inventaire["fraises"] = 76
inventaire["prunes"] = 51

#On met l'inventaire dans une liste pour tier
inventaireinverse = list()
for i, fruit in enumerate(inventaire):
    #print("{} - {} - {}".format(i, fruit, inventaire[fruit]))
    inventaireinverse.append((inventaire[fruit], fruit))

#for fruit in enumerate(inventaireinverse):
#    print(fruit)

#On inverse le tri
inventaireinverse.sort(reverse=True)

#On recrée le dictionnaire sur la liste triée
inventaire = dict()
for i, fruit in enumerate(inventaireinverse):
    inventaire[fruit[1]] = fruit[0]

for cle, fruit in enumerate(inventaire):
    print("{} - {} - {}".format(cle, fruit, inventaire[fruit]))


