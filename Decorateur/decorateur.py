# -*-coding:Latin-1 -*

import time

message="toto"

def afficheMessageAvecTemps(a_message):
    def decorateur(fonction_modifiee):
        def afficheMessageModifie(b_message):
            temps = time.time()
            chaine = "{} : "+str(b_message)
            print(chaine.format(temps))

            return fonction_modifiee
        return afficheMessageModifie(a_message)
    return decorateur

@afficheMessageAvecTemps(message)
def afficherMessage(message):
    """Affiche un message"""
    print(message)

