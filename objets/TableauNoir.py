# -*-coding:Latin-1 -*

class TableauNoir:
    """Classe d�finissant une surface sur laquelle on peut �crire,
    que l'on peut lire et effacer, par jeu de m�thodes. L'attribut modifi�
    est 'surface'"""

    nbTableaux=0

    def __init__(self):
        """Par d�faut, notre surface est vide"""
        self._surface=""
        TableauNoir.nbTableaux+=1

    def __repr__(self):
        return "Texte du tableau noir par repr : "+self._surface

    def __str__(self):
        return "Texte du tableau noir par str : "+self._surface

    def ecrire(self, message):
        print("ecrire")
        """Ajoute un message au tableau, avec un saut de ligne si le tableau n'est pas vide."""
        if len(self._surface) > 0:
            self._surface+="\n"

        self._surface+=message

    def lire(self):
        """Retourne les messages du tableau"""
        print("lire")
        return self._surface

    def effacer(self):
        """Efface le tebleau"""
        self._surface = ""

    def combienTableaux(cls):
        """M�thode de classe affichant combien d'objets ont �t� cr��s"""
        print("Jusqu'� pr�sent, {} tabeaux ont �t� cr��s.".format(
            cls.nbTableaux))
        #combienTableaux = classmethod(combienTableaux)

    surface = property(lire, ecrire)