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
        """Decompose le message reçu pour détecter l'action à efefctuer :
        SAI : Sélection de la map
        MAP : Affichage nom map
        ADD : Creation du joueur
        DEP : Déplacement
        DEB : Début de partie
        MUR : Crétion d'un mur
        DEL : Suppression d'un mur
        """
        message = "DEPXggenier(1,2,3)"
        self.assertEqual(utils.fonctions.actionAEffectuer(message), "DEP")

    def testDecomposeMessageAction(self):
        """Decompose le reste du message reçu er retourne les données utiles"""
        message = "DEPXggenier(1,2,3)"
        self.assertEqual(utils.fonctions.decomposeMessageAction(message), "Xggenier(1,2,3)")

unittest.main()