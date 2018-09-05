# -*-coding:Utf-8 -*
from map import Map

"""This module contains the Maze class"""


class Maze:
    def __init__(self, name, path):
        # Load the map of the maze
        self._map = Map(name, path)
        self._robot1, self._robot2 = self._map.getRobots()

        # define the statut of the game
        self._statut = "ingame"

    def __repr__(self):
        for idx, l in enumerate(self._map._box):
            if idx == self._robot1[0]:
                x1 = self._robot1[1]
                if idx == self._robot2[0]:
                    x2 = self._robot2[1]
                    if self._robot1[1] < self._robot2[1]:
                        print("".join(
                            [l[:x1], "1", l[x1+1:x2], "2", l[x2+1:]]), end="")
                    else:
                        print("".join(
                            [l[:x2], "2", l[x2+1:x1], "1", l[x1+1:]]), end="")

                else:
                    print("".join([l[:x1], "1", l[x1+1:]]), end="")
            elif idx == self._robot2[0]:
                x = self._robot2[1]
                print("".join([l[:x], "2", l[x+1:]]), end="")
            else:
                print(l, end="")

        print("\n")

    def getServerMap(self):
        # Get a string which contains the map with player on it
        str_map = ""
        for idx, l in enumerate(self._map._box):
            if idx == self._robot1[0]:
                x1 = self._robot1[1]
                if idx == self._robot2[0]:
                    x2 = self._robot2[1]
                    if self._robot1[1] < self._robot2[1]:
                        str_map += "".join(
                            [l[:x1], "1", l[x1+1:x2], "2", l[x2+1:]])
                    else:
                        str_map += "".join(
                            [l[:x2], "2", l[x2+1:x1], "1", l[x1+1:]])

                else:
                    str_map += "".join([l[:x1], "1", l[x1+1:]])
            elif idx == self._robot2[0]:
                x = self._robot2[1]
                str_map += "".join([l[:x], "2", l[x+1:]])
            else:
                str_map += l

        return str_map + "\n"

    def display(self):
        self.__repr__()

    def move(self, dir, player):
        # Move the robot if the direction is available
        val = dir[1:]
        if val == "":
            val = 1
        else:
            val = int(val)

        if player == 1:
            newPos = list(self._robot1)
        else:
            newPos = list(self._robot2)

        canMove = False
        if dir[0] == "O":
            newPos[1] -= val
            if self._map.getChar(newPos) in " .U":
                canMove = True
        elif dir[0] == "E":
            newPos[1] += val
            if self._map.getChar(newPos) in " .U":
                canMove = True
        elif dir[0] == "N":
            newPos[0] -= val
            if self._map.getChar(newPos) in " .U":
                canMove = True
        elif dir[0] == "S":
            newPos[0] += val
            if self._map.getChar(newPos) in " .U":
                canMove = True

        if canMove:
            if player == 1:
                self._robot1 = newPos
            else:
                self._robot2 = newPos
        else:
            print("Impossible to walk on {}".format(self._map.getChar(newPos)))
            return 2

        return 0

    def edit(self, dir, player):
        action = dir[0]
        # Place a wall or a door if the position is available
        dir = dir[1:]
        val = dir[1:]
        if val == "":
            val = 1
        else:
            val = int(val)

        if player == 1:
            newPos = list(self._robot1)
        else:
            newPos = list(self._robot2)

        canEdit = False
        if dir[0] == "O":
            newPos[1] -= val
            if self._map.getChar(newPos) == "." and action == "M":
                canEdit = True
            if self._map.getChar(newPos) == "O" and action == "P":
                canEdit = True
        elif dir[0] == "E":
            newPos[1] += val
            if self._map.getChar(newPos) == "." and action == "M":
                canEdit = True
            if self._map.getChar(newPos) == "O" and action == "P":
                canEdit = True
        elif dir[0] == "N":
            newPos[0] -= val
            if self._map.getChar(newPos) == "." and action == "M":
                canEdit = True
            if self._map.getChar(newPos) == "O" and action == "P":
                canEdit = True
        elif dir[0] == "S":
            newPos[0] += val
            if self._map.getChar(newPos) == "." and action == "M":
                canEdit = True
            if self._map.getChar(newPos) == "O" and action == "P":
                canEdit = True

        if action == "P":
            wall = "."
        else:
            wall = "O"

        if canEdit:
            str = self._map._box[newPos[0]]
            str = "".join([str[:newPos[1]], wall, str[newPos[1]+1:]])
            self._map._box[newPos[0]] = str
        else:
            print("You can't do that here")
            return 2

        return 0

    # Check if the command is correct
    def execute(self, string, playr):
        # Format of a message : !PLAYER:MESSAGE
        # Check if the structure is correct
        correct_struct = False
        if string[0] == "!" and string[1] in ["1", "2"] and string[2] == ":":
            correct_struct = True

        if not correct_struct:
            return -1

        if int(string[1]) != playr:
            return 1

        player = int(string[1])
        string = string[3:]
        # If it is, move or edit the map
        print(string)
        if string.upper()[0] in ["O", "N", "E", "S"]:
            return self.move(string.upper(), player)
        elif string.upper()[0] in ["M", "P"]:
            return self.edit(string.upper(), player)
        else:
            return 3

    def getWinner(self):
        # Check if a player is on the U
        if self._map.getChar(self._robot1) == "U":
            return 1
        elif self._map.getChar(self._robot2) == "U":
            return 2
        else:
            return 0
