# -*-coding:Latin-1 -*

from Iterateur.RevStr import RevStr

chaine = RevStr("123456789")
iter_chaine = iter(chaine)
i=len(chaine)
while i > 0:
    print(next(iter_chaine))
    i-=1

chaine = RevStr("123456789")
print("Parcours avec for")
for caractere in chaine:
    print(caractere)