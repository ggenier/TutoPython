# -*-coding:Latin-1 -*

import unittest
from labyrinthe.Obstacle import Obstacle

class ObstacleTest(unittest.TestCase):
    """Test case de la classe obstacle"""

    def testCreation(self):
        """Test la creation de l'objet"""

        obstacle = Obstacle("M", True, "O")

        #On vérifie que l'objet est non nul
        self.assertIsNotNone(obstacle)

unittest.main()