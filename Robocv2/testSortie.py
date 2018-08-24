# -*-coding:Latin-1 -*

import unittest
from labyrinthe.Obstacle import Obstacle
from labyrinthe.Sortie import Sortie

class SortieTest(unittest.TestCase):
    """Test case de la classe obstacle"""

    def setUp(self):
        self.sortie = Sortie()

    def testCreation(self):
        """Test la creation de l'objet"""

        #On vérifie que l'objet est une instance de Obstable
        self.assertIsInstance(self.sortie, Obstacle)

    def testType(self):
        """Test si le type est bien S"""

        #On vérifie que l'objet est une sortie
        self.assertEqual(self.sortie.getType(), "S")

    def testBloquant(self):
        """Test si le Sortie est bien bloquant"""

        #On vérifie que l'objet est un Sortie
        self.assertFalse(self.sortie.getBloquant())

unittest.main()