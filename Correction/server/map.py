# -*-coding:Utf-8 -*

import random
"""This module contains the Map class"""


class Map:
    """Object which contains only the map"""

    def __init__(self, name, path):
        # Load the map using its path in _box
        self._name = name
        self._path = path

        with open(path, "r") as file:
            self._box = file.readlines()

    def __repr__(self):
        return "Map <{}>".format(self.name)

    def getRobots(self):
        # Get 2 positiions on the map and return it
        available_places = []
        for i, l in enumerate(self._box):
            for j, c in enumerate(l):
                if c == " ":
                    available_places.append([i, j])

        robot1_pos, robot2_pos = random.sample(available_places, 2)

        return robot1_pos, robot2_pos

    def getChar(self, pos):
        # Return the character at the coordinate of pos
        if type(pos) is not list or len(pos) is not 2:
            raise TypeError
        else:
            if pos[0] < 0 or pos[0] >= len(self._box):
                return "O"
            if pos[1] < 0 or pos[1] >= len(self._box[0]):
                return "O"

            return self._box[pos[0]][pos[1]]
