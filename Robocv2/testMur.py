# -*-coding:Latin-1 -*

import unittest
from labyrinthe.Obstacle import Obstacle
from labyrinthe.Mur import Mur

class MurTest(unittest.TestCase):
    """Test case de la classe obstacle"""

    def setUp(self):
        self.mur = Mur()

    def testCreation(self):
        """Test la creation de l'objet"""

        #On vérifie que l'objet est une instance de Obstable
        self.assertIsInstance(self.mur, Obstacle)

    def testType(self):
        """Test si le type est bien M"""

        #On vérifie que l'objet est un mur
        self.assertEqual(self.mur.getType(), "M")

    def testBloquant(self):
        """Test si le mur est bien bloquant"""

        #On vérifie que l'objet est un mur
        self.assertTrue(self.mur.getBloquant())

unittest.main()