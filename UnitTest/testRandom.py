# -*-coding:Latin-1 -*

import random
import unittest

class RandomTest(unittest.TestCase):
    """Test case de la fonction std random"""

    def setUp(self):
        self.liste = list(range(10))

    def testChoice_OK(self):
        """Test le fonctionnement de la focntion choice"""

        #on tire un �lement au hasard
        elt = random.choice(self.liste)

        #On v�rifie qu'il est bien dans la liste
        self.assertIn(elt, self.liste)

    def testSuffle_OK(self):
        """Test le fonctionnement de la fonction choice"""

        #On consrtuit une liste
        listeOrig = list(range(10))

        #On m�lange la liste
        random.shuffle(self.liste)

        #On v�rifie que le deux listes sont diff�rentes
        self.assertNotEqual(listeOrig, self.liste)

    def testSample_OK(self):
        """Test le fonctionnement de la fonction sample"""

        #On consrtuit une liste
        listeOrig = list(range(10))

        #On s�lectionne un �chantillon
        sample = random.sample(self.liste, 2)
        sampleOrig = random.sample(listeOrig, 2)

        #On v�rifie que le deux sample sont diff�rents
        self.assertNotEqual(sample, sampleOrig)

    def testSample_KO(self):
        """Test le fonctionnement de la fonction sample"""

        #On consrtuit une liste
        listeOrig = list(range(10))

        #On s�lectionne un �chantillon
        sample = random.sample(self.liste, 2)
        sampleOrig = random.sample(listeOrig, 2)

        #On v�rifie que le deux sample sont diff�rents
        self.assertNotEqual(sample, sampleOrig)

        #On test avec un �chantillon de plus grande taille que notre liste.
        #Cela doit lever une exception
        with self.assertRaises(ValueError):
            random.sample(self.liste, 20)

    def testSuffle_KO(self):
        """Test le fonctionnement de la focntion choice"""

        #On consrtuit une liste
        listeOrig = list(range(10))

        #On ne m�lange pas la liste pour provoquer une erreur
        #random.shuffle(liste)

        #On v�rifie que le deux listes sont diff�rentes
        self.assertNotEqual(listeOrig, self.liste)

    def testChoice_KO(self):
        """Test le fonctionnement de la focntion choice"""

        # on tire un �lement au hasard
        elt = random.choice(self.liste)

        # On v�rifie qu'il est bien dans la liste
        self.assertIn(str(elt), ("a, b, c"))

#Ne pas mettre cette ligne si on lance les tests depuis la consolse avec : python -m unittest
#Le nom d fichier de tests doit commencer par test
#unittest.main()