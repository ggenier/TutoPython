# -*-coding:Latin-1 -*

def formatMontant(montant, nbdec):
    positionpoint = montant.find(".")
    entier = montant[0:int(positionpoint)]
    decimal = montant[int(positionpoint)+1:int(positionpoint)+1+nbdec]
    montant = str(entier)+"."+str(decimal)
    montant = montant.replace(".", ",")
    return montant

def formatMontant2(montant, nbdec):
    try:
        montant = float(montant)
    except:
        "Float obligatoire"

    montantsplit = str(montant).split(".")
    return ",".join([montantsplit[0], montantsplit[1][0:nbdec]])

print(formatMontant("3.999999", 3))
print(formatMontant2("3.999999", 4))