# -*-coding:Latin-1 -*

class Personne:

    def __init__(self, nom, prenom, age, adresse):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.adresse = adresse

    def __str__(self):
        return "{} {}, age {}, adresse {}".format(self.nom, self.prenom, self.age, self.adresse)

