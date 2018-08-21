
def estBissextile(annee = 1900):
    annee = int(annee)
    reste = annee % 4

    estBissextile = False
    if annee == 0: #Multiple de 4
        reste = annee % 100
        if reste == 0: #Multiple de 100
            reste = annee % 400
            if reste == 0: #Multiple de 400
                estBissextile = True

    return estBissextile

