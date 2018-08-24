# -*-coding:Latin-1 -*

import unittest
from labyrinthe.Obstacle import Obstacle
from labyrinthe.Porte import Porte

class PorteTest(unittest.TestCase):
    """Test case de la classe obstacle"""

    def setUp(self):
        self.porte = Porte()

    def testCreation(self):
        """Test la creation de l'objet"""

        #On vérifie que l'objet est une instance de Obstable
        self.assertIsInstance(self.porte, Obstacle)

    def testType(self):
        """Test si le type est bien P"""

        #On vérifie que l'objet est une porte
        self.assertEqual(self.porte.getType(), "P")

    def testBloquant(self):
        """Test si le mur est bien bloquant"""

        #On vérifie que l'objet est un mur
        self.assertFalse(self.porte.getBloquant())

unittest.main()