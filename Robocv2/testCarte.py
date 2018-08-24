# -*-coding:Latin-1 -*

import unittest
from labyrinthe.Carte import Carte
import utils.affichage


class testCarte(unittest.TestCase):
    """Test case de la classe Carte"""

    def setUp(self):
        self.carte = Carte("maps/facile.txt")

    def testCheminCarte(self):
        self.assertEqual(self.carte.getCheminCarte(), "maps/facile.txt")

    def testAnalyse(self):
        self.carte.analyseCarte()
        self.assertIsNotNone(self.carte.getStructureCarte())

    def testAffichageCarte(self):
        self.carte.analyseCarte()
        utils.affichage.affichageStructureCarte(self.carte.getStructureCarte())

unittest.main()


