# -*-coding:Latin-1 -*

import unittest
from Joueur import Joueur
from labyrinthe.Obstacle import Obstacle

class SortieTest(unittest.TestCase):
    """Test case de la classe Joueur"""

    def setUp(self):
        self.joueur = Joueur("tPseudo", "X")

    def testCreation(self):
        """Test la creation de l'objet"""

        #On vérifie que l'objet est une instance de Obstacle
        self.assertIsInstance(self.joueur, Obstacle)

    def testType(self):
        """Test si le type est bien J"""

        #On vérifie que l'objet est un joueur
        self.assertEqual(self.joueur.getType(), "J")

    def testBloquant(self):
        """Test si le joueur est bien bloquant"""

        #On vérifie que l'objet est un Sortie
        self.assertTrue(self.joueur.getBloquant())

unittest.main()