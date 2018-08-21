# -*-coding:Latin-1 -*

from objets.Personne import Personne

class AgentSpecial(Personne):

    def __init__(self, nom, prenom, age, adresse, matricule):
        Personne.__init__(self, nom, prenom, age, adresse)
        self.matricule = matricule

    def __str__(self):
        return "Agent special {} {}, age {}, adresse {}, matricule {}".format(self.nom, self.nom, self.age, self.adresse, self.matricule)