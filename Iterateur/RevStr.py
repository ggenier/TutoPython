# -*-coding:Latin-1 -*

from Iterateur.ItRevStr import ItRevStr

class RevStr(str):
    """Classe h�ritant de str permettant de parcourir une chaien de droite � gauche"""

    def __init__(self, chaine):
        str.__init__(chaine)
        self.chaine = chaine

    def __iter__(self):
        """Calcul un nouvel it�rateur sur la chaine"""
        print("Calcul it�rateur")
        return ItRevStr(self.chaine)
