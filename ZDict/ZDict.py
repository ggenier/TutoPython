class ZDict:
    def __init__(self):
        self._dictionnaire = dict()

    def __getitem__(self, item):
        print("accès objet")
        return self._dictionnaire[item]

    def __setitem__(self, key, value):
        print("Ajout objet")
        self._dictionnaire[key] = value

    def __contains__(self, item):
        print("Test IN objet")
        if item in self._dictionnaire:
            return True
        else:
            return False

    def __len__(self):
        print("Test taille objet")
        return len(self._dictionnaire)

    def __str__(self):
        chaine="Contenu du dictionnaire : "
        for indice, cle in enumerate(self._dictionnaire):
            chaine+="\n"+cle + " - " + self._dictionnaire[cle]

        return chaine

zdict = ZDict()
zdict["test1"] = "Test 1"
zdict["test2"] = "Test 2"
print("Element 1 de zdict : "+zdict["test1"])
print("Info objet : \n"+str(zdict))

if "test1" in zdict:
    print("Est dans zdict")
else:
    print("N'est pas dans zdict")

print("Taille zdict : "+str(len(zdict)))