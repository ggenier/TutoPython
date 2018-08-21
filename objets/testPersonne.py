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

status = 100
if status != 0:
    raise MonException("select bkcom", status)