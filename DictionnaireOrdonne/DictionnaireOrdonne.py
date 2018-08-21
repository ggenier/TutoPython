# -*-coding:Latin-1 -*

class DictionnaireOrdonne:
    """Classe permettant de g�rer un dictionnaire ordonn�. LE dictionnaire sera tri� selon les cl�s"""

    def __init__(self, *paramNonNommes, **paramNommes):
        """Constructeur � partir de param�tres cle=valeur ou dictionnaire"""
        self.listeCle = list()
        self.listeValeur = list()

        if isinstance(paramNommes, dict):
            for cle in paramNommes:
                self.listeCle.append(cle)
                self.listeValeur.append(paramNommes[cle])

        #Fonctionne pas, on re�oit un seul tuple avec toutes les valeurs dans un seul typle
        #il faudrait retraiter la chaine pour d�couper les tuples

        #if paramNonNommes is not None:
            #print(len(paramNonNommes))
            #for indice, couple in enumerate(paramNonNommes):
               # print(str(indice)+str(couple))
             #   self.listeCle.append(cle)
              #  self.listeValeur.append(paramNonNommes[cle])

    def __getitem__(self, item):
        """Retourne la valeur de la cl� recherch�e"""
        indice = self.recupNbIndex(item)
        valeur =""
        if indice < len(self.listeCle):
            valeur = self.listeValeur[indice]

        return valeur

    def recupNbIndex(self, key):
        """Retourne l'indice de la cl� recherch�e"""
        indice = 0
        for cle in self.listeCle:
            if str(cle) == str(key):
                break
            indice+=1

        return indice

    def __setitem__(self, key, value):
        """Permet de modifier la valeur d'une cl�.
        Si la cl� n'existe pas, elle est ajout� au dictionnaire"""
        indice = self.recupNbIndex(key)
        if indice >= len(self.listeCle):
            #Nouvelle valeur
            self.listeCle.append(key)
            self.listeValeur.append(value)
        else:
            #Donn�e existante on la modifie
            self.listeValeur[indice] = value

    def __delitem__(self, key):
        """Supprime un �l�ment du dictionnaire"""
        indice = self.recupNbIndex(key)
        del(self.listeValeur[indice])
        del(self.listeCle[indice])

    def __contains__(self, item):
        """Retourne True si l'item fait parti du dictionnaire"""
        trouve = False
        indice = self.recupNbIndex(item)
        if indice < len(self.listeCle):
            trouve = True

        return trouve

    def __len__(self):
        """Retourne la taille du dictionnaire"""
        return len(self.listeCle)

    def keys(self):
        """Retourne les cl� du dictionnaire via un g�n�rateur"""
        for cle in self.listeCle:
            yield cle

    def values(self):
        """Retourne les valeur du dictionnaire via un g�n�rateur"""
        for valeur in self.listeValeur:
            yield valeur

    def items(self):
        """Retourne des tuples cl�s/valeurs via un g�n�rateur"""
        for cle in self.listeCle:
            indice = self.recupNbIndex(cle)
            yield (cle, self.listeValeur[indice])

    def __add__(self, other):
        """Permet d'ajouter un DictionnaireOrdonn�, les nouvelles valeurs se retrouvent � la fin.
        Si deux cl�s sont pr�sentent dans les deux listes, la nouvelle valeur sera prise en compte"""
        if isinstance(other, DictionnaireOrdonne):
            for item in other.items():
                self.__setitem__(item[0], item[1])
        else:
            raise TypeError("DictionnaireOrdonne attendu")

        return self

    def sort(self):
        """Tri le dictionnaire sur les cl�s"""
        backupListeCle = list()
        for cle in self.listeCle:
            backupListeCle.append(cle)

        #Tri de la liste des cl�s
        self.listeCle.sort()

        #On parcours la liste des cl�s
        nouvelleValeur = ""
        nouvelleListeValeur = list()
        for cle in self.listeCle:
            #On recherche l'ancien indice de cette cl�
            ancienIndiceValeur = 0
            for backupCle in backupListeCle:
                if backupCle == cle:
                    nouvelleValeur = self.listeValeur[ancienIndiceValeur]
                    break

                ancienIndiceValeur+=1

            #On cr�er la nouvelle liste de valeur
            nouvelleListeValeur.append(nouvelleValeur)

        #On �crase l'ancienne liste
        self.listeValeur = nouvelleListeValeur

    def reverse(self):
        """Inverse le dictionnaire sur les cl�s"""
        nouvelleListeCle = list()
        nouvelleListeValeur = list()

        taille = len(self.listeCle)
        while taille > 0:
            nouvelleListeCle.append(self.listeCle[taille-1])
            nouvelleListeValeur.append(self.listeValeur[taille - 1])
            taille-=1

        self.listeCle = nouvelleListeCle
        self.listeValeur = nouvelleListeValeur

    def __str__(self):
        """Formattage du dictionnaire pour affichage"""
        chaine="{"
        indice=0
        for cle in self.listeCle:
            chaine += "'" + cle + "' : " + str(self.listeValeur[indice])
            if indice != len(self.listeCle)-1:
                chaine += ", "

            indice+=1

        chaine += "}"
        return chaine