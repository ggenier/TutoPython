# -*-coding:Latin-1 -*

class MonException(Exception):
    def __init__(self, message, status):
        self.message = message
        self.status = status

    def __str__(self):
        return "Erreur : {} status {}".format(self.message, self.status)