# -*-coding:Latin-1 -*

import TutoThread.thread

#On crée les deux Thread
afficheur1=TutoThread.thread.Afficheur("calcul")
afficheur2=TutoThread.thread.Afficheur("ZOMBIE")

#On lance les Thread
afficheur1.start()
afficheur2.start()

#On attend qu'ils se finissent
afficheur1.join()
afficheur2.join()