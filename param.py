# -*-coding:Latin-1 -*

def print2(*value, sep=' ', fin='\n'):
    chaine = str()
    for elt in value:
        chaine = sep.join([elt, chaine])

    chaine += fin
    print(chaine)

print2("TOTO", "TITI", "TUTU", sep=',', fin="*")