# -*-coding:Latin-1 -*

class ItRevStr:

    def __init__(self, chaine):
        self.chaine = chaine
        self.position = len(chaine)

    def __next__(self):
        #print("Next caracter : "+str(self.position))
        if self.position == 0:
            raise StopIteration(self, "Fin chaine")

        caractere = self.chaine[self.position-1]
        #print("Caracter readed : " + caractere)
        self.position-=1
        return caractere