# -*-coding:Latin-1 -*

"""A lancer dans l'interpr�teur pas un IDE (ou terminal python de l'IDE"""
import signal
import sys

def fermer_programme(signa, frame):
    """Fonction appel�e � la fermeture du programme"""

    print("Fermeture programme")
    sys.exit(0)

signal.signal(signal.SIGINT, fermer_programme)

while True:
    pass