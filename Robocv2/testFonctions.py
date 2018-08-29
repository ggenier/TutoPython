# -*-coding:Latin-1 -*

import unittest
import utils.fonctions


class testFonctions(unittest.TestCase):
    """Test case de la classe fonctions communes"""

    def testDecomposeMessageDeplacement(self):
        deplacementDemande="Xggenier(1,2,3)"
        representation, pseudo, positions = utils.fonctions.decomposeMessageDeplacement(deplacementDemande)

        self.assertEqual(representation, "X")
        self.assertEqual(pseudo, "ggenier")
        self.assertEqual(positions[0], '1')
        self.assertEqual(positions[1], '2')
        self.assertEqual(positions[2], '3')


    def testActionAEffectuer(self):
        """Decompose le message re�u pour d�tecter l'action � efefctuer :
        SAI : S�lection de la map
        MAP : Affichage nom map
        ADD : Creation du joueur
        DEP : D�placement
        DEB : D�but de partie
        MUR : Cr�tion d'un mur
        DEL : Suppression d'un mur
        """
        message = "DEPXggenier(1,2,3)"
        self.assertEqual(utils.fonctions.actionAEffectuer(message), "DEP")

    def testDecomposeMessageAction(self):
        """Decompose le reste du message re�u er retourne les donn�es utiles"""
        message = "DEPXggenier(1,2,3)"
        self.assertEqual(utils.fonctions.decomposeMessageAction(message), "Xggenier(1,2,3)")

unittest.main()