# -*-coding:Latin-1 -*

from objets.Personne import Personne
from objets.AgentSpecial import AgentSpecial
from objets.MonException import MonException

moi = Personne("GENIER", "GREGOIRE", 36, "TOURS")
print(str(moi))

moi2 = AgentSpecial("GENIER1", "GREGOIRE1", 36, "TOURS1", "1234-56-78")
print(str(moi2))

print("moi est une instance de Personne : "+str(isinstance(moi, Personne)))
print("moi est une instance de AgentSpecial : "+str(isinstance(moi, Personne)))

print("moi2 est une instance de Personne : "+str(isinstance(moi2, Personne)))
print("moi2 est une instance de AgentSpecial : "+str(isinstance(moi2, Personne)))

print("Personne hérite de AgentSpecial : "+str(issubclass(Personne, AgentSpecial)))
print("AgentSpecial hérite de AgentSpecial : "+str(issubclass(AgentSpecial, Personne)))

listePersonne=list()
listePersonne.append(moi)
print("print(listePersonne[0]) "+str(listePersonne[0]))
quelquun = listePersonne[0]
quelquun.nom="TOTO"
print("print(listePersonne[0]) "+str(listePersonne[0]))

moi3=moi
listePersonne.append(moi3)
print("2 print(listePersonne[1]) "+str(listePersonne[1]))
moi3.nom="TUTU"
print("2 print(listePersonne[1]) "+str(listePersonne[1]))
print("2 print(listePersonne[0]) "+str(listePersonne[0]))