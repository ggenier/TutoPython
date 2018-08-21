import estBissextile

annee=1900
while annee != 0:
    annee = input("Saisissez une année : ")
    try:
        assert annee>0
    except TypeError as erreur: #N'arrete pas l'execution, faut mettre un break
        print("Annee incorrect 0 ", erreur)
        raise("Annee incorrect raise 0 ", erreur)

    try:
        annee = int(annee)
    except TypeError as erreur:
        print("Annee incorrect 1 ", erreur)
        break
    except NameError as erreur:
        print("Annee incorrect 2 ", erreur)
        break
    except ValueError as erreur:
        print("Annee incorrect 3 ", erreur)
        break
    finally: #tjs exécuté si exception
        print("Fin try")
        break

    reste = annee % 4
    if estBissextile.estBissextile(annee):
        print("Annee bissextile")
    else:
        print("Annee non bissextile")