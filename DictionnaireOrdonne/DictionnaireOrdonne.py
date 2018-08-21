# -*-coding:Latin-1 -*

class DictionnaireOrdonne:
    """Classe permettant de gérer un dictionnaire ordonné. LE dictionnaire sera trié selon les clés"""

    def __init__(self, *paramNonNommes, **paramNommes):
        """Constructeur à partir de paramètres cle=valeur ou dictionnaire"""
        self.listeCle = list()
        self.listeValeur = list()

        if isinstance(paramNommes, dict):
            for cle in paramNommes:
                self.listeCle.append(cle)
                self.listeValeur.append(paramNommes[cle])

        #Fonctionne pas, on reçoit un seul tuple avec toutes les valeurs dans un seul typle
        #il faudrait retraiter la chaine pour découper les tuples

        #if paramNonNommes is not None:
            #print(len(paramNonNommes))
            #for indice, couple in enumerate(paramNonNommes):
               # print(str(indice)+str(couple))
             #   self.listeCle.append(cle)
              #  self.listeValeur.append(paramNonNommes[cle])

    def __getitem__(self, item):
        """Retourne la valeur de la clé recherchée"""
        indice = self.recupNbIndex(item)
        valeur =""
        if indice < len(self.listeCle):
            valeur = self.listeValeur[indice]

        return valeur

    def recupNbIndex(self, key):
        """Retourne l'indice de la clé recherchée"""
        indice = 0
        for cle in self.listeCle:
            if str(cle) == str(key):
                break
            indice+=1

        return indice

    def __setitem__(self, key, value):
        """Permet de modifier la valeur d'une clé.
        Si la clé n'existe pas, elle est ajouté au dictionnaire"""
        indice = self.recupNbIndex(key)
        if indice >= len(self.listeCle):
            #Nouvelle valeur
            self.listeCle.append(key)
            self.listeValeur.append(value)
        else:
            #Donnée existante on la modifie
            self.listeValeur[indice] = value

    def __delitem__(self, key):
        """Supprime un élément du dictionnaire"""
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
        """Retourne les clé du dictionnaire via un générateur"""
        for cle in self.listeCle:
            yield cle

    def values(self):
        """Retourne les valeur du dictionnaire via un générateur"""
        for valeur in self.listeValeur:
            yield valeur

    def items(self):
        """Retourne des tuples clés/valeurs via un générateur"""
        for cle in self.listeCle:
            indice = self.recupNbIndex(cle)
            yield (cle, self.listeValeur[indice])

    def __add__(self, other):
        """Permet d'ajouter un DictionnaireOrdonné, les nouvelles valeurs se retrouvent à la fin.
        Si deux clés sont présentent dans les deux listes, la nouvelle valeur sera prise en compte"""
        if isinstance(other, DictionnaireOrdonne):
            for item in other.items():
                self.__setitem__(item[0], item[1])
        else:
            raise TypeError("DictionnaireOrdonne attendu")

        return self

    def sort(self):
        """Tri le dictionnaire sur les clés"""
        backupListeCle = list()
        for cle in self.listeCle:
            backupListeCle.append(cle)

        #Tri de la liste des clés
        self.listeCle.sort()

        #On parcours la liste des clés
        nouvelleValeur = ""
        nouvelleListeValeur = list()
        for cle in self.listeCle:
            #On recherche l'ancien indice de cette clé
            ancienIndiceValeur = 0
            for backupCle in backupListeCle:
                if backupCle == cle:
                    nouvelleValeur = self.listeValeur[ancienIndiceValeur]
                    break

                ancienIndiceValeur+=1

            #On créer la nouvelle liste de valeur
            nouvelleListeValeur.append(nouvelleValeur)

        #On écrase l'ancienne liste
        self.listeValeur = nouvelleListeValeur

    def reverse(self):
        """Inverse le dictionnaire sur les clés"""
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