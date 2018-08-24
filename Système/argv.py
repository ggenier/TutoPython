# -*-coding:Latin-1 -*

"""Utilisation arguments lignes de commandes, et gestion des options
A lancer dans l'interpréteur pas un IDE (ou terminal python de l'IDE"""

import sys
import argparse

print(sys.argv)

#Parser les arguments pour avoir les options
parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="Nombre à multiplier")
parser.add_argument("y", type=int, help="Nombre à multiplier")
parser.add_argument("-v", "--verbose", action="store_true", help="Détail du calcul")
arguments=parser.parse_args()
if arguments.verbose:
    print("Résultat {}*{}: {}".format(arguments.x, arguments.y, arguments.x*arguments.y))
else:
    print(arguments.x*arguments.y)