# -*-coding:Latin-1 -*

import unittest
import utils.affichage


class testAffichage(unittest.TestCase):
    """Test case de la classe fonctions communes"""

    def testSaisieNonValide(self):
        saisieValide, direction, nbDeplacement = utils.affichage.controleSaisieDirection("w")

        self.assertFalse(saisieValide)

    def testCreationMurOK(self):
        saisieValide, direction, nbDeplacement = utils.affichage.controleSaisieDirection("mn")

        self.assertTrue(saisieValide)
        self.assertEqual(direction, "n")
        self.assertEqual(nbDeplacement, "m")

    def testCreationMurKO(self):
        saisieValide, direction, nbDeplacement = utils.affichage.controleSaisieDirection("m")

        self.assertFalse(saisieValide)

    def testDeplacementOK(self):
        saisieValide, direction, nbDeplacement = utils.affichage.controleSaisieDirection("n")

        self.assertTrue(saisieValide)
        self.assertEqual(direction, "n")
        self.assertEqual(nbDeplacement, "1")

    def testDeplacementOK_2(self):
        saisieValide, direction, nbDeplacement = utils.affichage.controleSaisieDirection("s3")

        self.assertTrue(saisieValide)
        self.assertEqual(direction, "s")
        self.assertEqual(nbDeplacement, "3")


unittest.main()