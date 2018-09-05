import random
import unittest
import sys
sys.path.append("..")

import network


class NetworkTest(unittest.TestCase):
    def test_getMessage(self):
        lett = "abcdefijklmnopqrstuvwxyz0123456789<>:!"
        nb = random.randrange(2, len(lett))
        str = "".join(random.sample(lett, nb))

        res = network.getMessage(str)
        self.assertIn(res[0], [-1, 0, 1, 2, 3, 4])
