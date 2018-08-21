# -*-coding:Latin-1 -*

from Iterateur.ItRevStr import ItRevStr

class RevStr(str):
    """Classe héritant de str permettant de parcourir une chaien de droite à gauche"""

    def __init__(self, chaine):
        str.__init__(chaine)
        self.chaine = chaine

    def __iter__(self):
        """Calcul un nouvel itérateur sur la chaine"""
        print("Calcul itérateur")
        return ItRevStr(self.chaine)
