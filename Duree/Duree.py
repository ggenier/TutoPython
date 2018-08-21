class Duree:
    def __init__(self, min=0, sec=0):
        self.heure = 0
        self.min = min
        self.sec = sec

    def __str__(self):
        return "{0:02}:{1:02}:{2:02}".format(self.heure, self.min, self.sec)

    def __add__(self, other):
        """L'objet à ajouter est un entier, le nombre de secondes"""
        if isinstance(other , Duree):
            print("add de 2 duree")
            nouvelle_min = self.min + other.min
            nouvelle_sec = self.sec + other.sec
            nouvelle_heure = 0

            if nouvelle_sec >= 60:
                nouvelle_sec = nouvelle_sec - 60
                nouvelle_min += 1

            print("nouvelle_min : " + str(nouvelle_min))
            if nouvelle_min >= 60:
                nouvelle_min = nouvelle_min - 60
                nouvelle_heure += 1

            nouvelle_duree = Duree(nouvelle_min, nouvelle_sec)
            nouvelle_duree.heure = nouvelle_heure

        else:
            nouvelle_duree = Duree()
            # On va copier self dans l'objet créé pour avoir la même durée
            nouvelle_duree.min = self.min
            nouvelle_duree.sec = self.sec
            # On ajoute la durée
            nouvelle_duree.sec += other
            # Si le nombre de secondes >= 60
            if nouvelle_duree.sec >= 60:
                nouvelle_duree.min += nouvelle_duree.sec // 60
                nouvelle_duree.sec = nouvelle_duree.sec % 60

        # On renvoie la nouvelle durée
        return nouvelle_duree

duree = Duree(10, 20)
duree = duree + 10
print("duree : "+str(duree))
duree = duree + 60
print("duree : "+str(duree))
duree2 = Duree(59, 59)
print("duree2 : "+str(duree2))
duree3 = duree+duree2
print("duree3 : "+str(duree3))