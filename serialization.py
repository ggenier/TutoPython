# -*-coding:Latin-1 -*

import pickle

inventaire = dict()
inventaire["pommes"] = 22
inventaire["melons"] = 4
inventaire["poires"] = 18
inventaire["fraises"] = 76
inventaire["prunes"] = 51

with open("c:/tmp/gg/pickle.txt",  'wb') as fichier:
    objpickle = pickle.Pickler(fichier)
    objpickle.dump(inventaire)

with open("c:/tmp/gg/pickle.txt", 'rb') as fichier:
        objpickle = pickle.Unpickler(fichier)
        inventaire =  objpickle.load()
        for i, invent in enumerate(inventaire):
            print(invent,"-",inventaire[invent])
