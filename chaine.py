# -*-coding:Latin-1 -*
chaine="bonjour"
print("chaine : "+chaine[:3])

prenom = "GREGOIRE"
nom = "GENIER"
age = "36"

chaine = """Je suis {nom} {prenom}, et j'ai {age} ans"""
print(chaine.format(nom=nom, prenom=prenom, age=age))

for carac in chaine:
    print("carac : "+carac)

i=0
while i <= len(chaine):
    print("carac : " + chaine[i])
    i+=1


