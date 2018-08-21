# -*-coding:Latin-1 -*

inventaire = [("pommes", 22), ("melons", 4), ("poires", 18), ("fraises", 76), ("prunes", 51)]
nouveauinventaire=list()

[nouveauinventaire.append([fruit[1], fruit[0]]) for i, fruit in enumerate(inventaire)]

#for fruit in enumerate(nouveauinventaire):
#    print(fruit)

nouveauinventaire.sort(reverse=True)
inventaire=nouveauinventaire
for fruit in enumerate(inventaire):
    print(fruit)
