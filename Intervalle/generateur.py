# -*-coding:Latin-1 -*

def intervalle(borne_inf, borne_sup):
    borne_inf += 1
    while borne_inf < borne_sup:
        yield borne_inf
        borne_inf += 1


for nb in intervalle(5, 10):
    print(nb)

print("Generateur reverse chaine")
def reverseStr(chaine):
    i=len(chaine)

    while i > 0:
        i-=1
        valeur_recue = (yield chaine[i])
        if valeur_recue is not None:
            i=valeur_recue


chaine = "123456789"
for caract in reverseStr(chaine):
    print(caract)

print("Generateur fermeture avant la fin du parcours")
generateur=reverseStr(chaine)
for caract in generateur:
    if int(caract)<5:
        generateur.close()

    print(caract)


print("Generateur envoi de valeur au générateur")
generateur=reverseStr(chaine)
for caract in generateur:
    if int(caract) == 5:
        #On va sauter 4, 3, 2
        generateur.send(2)

    print(caract)