# -*-coding:Utf-8 -*

"""
This file is the main one

Execute it to start the server
"""

# Import the maze
import os
import socket
import select
import time

import network
from maze import Maze

# Make a list of all maps with their path
maps = []
ret = True
maze = None
for file in os.listdir("./cartes"):
    if file.endswith(".txt"):
        path = os.path.join("cartes", file)
        mapName = file[:-4].lower()
        maps.append((mapName, path))

# we print all maps and ask the player to choose one
print("Maze(s) found :")
for i, map in enumerate(maps):
    print("  {} - {}".format(i + 1, maps[i][0]))

print("Choose a map to start")
ans = 0
while ans < 1 or ans > len(maps):
    ans = int(input("> "))
    if ans >= 1 and ans <= len(maps):
        maze = Maze(maps[ans-1][0], maps[ans-1][1])
    else:
        print("Error, {} is not a valid answer".format(ans))
        ans = 0

# Start a connection
main_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_connection.bind(("", 12800))
main_connection.listen(2)
print("Waiting for clients...")
waiting_players = True
waiting_start = False
waiting_command = False
isPlaying = 0

server_started = True
clients = []

while server_started:
    while waiting_players:
        asked_connection, wlist, xlist = select.select(
            [main_connection], [], [], 0.05)

        # Wait 2 clients
        for co in asked_connection:
            if len(clients) < 2:
                client, info = co.accept()
                clients.append(client)
                print("Waiting for another player")
                str = "Welcome player {}\n".format(len(clients))
                client.send(str.encode())

        if len(clients) == 2:
            time.sleep(0.3)
            waiting_players = False
            waiting_start = True
            print("Waiting to start")
            network.sendTo(clients, "Write 'C' to start\n")

    while waiting_start:
        # When 2 clients are here, start the game
        clients_to_read = []
        clients_to_read, wlist, xlist = select.select(clients, [], [], 0.5)
        for client in clients_to_read:
            msg = client.recv(1024)
            msg = msg.decode()
            # Print the client and the message sent
            print("[{}] : {}".format(client, msg))
            msg = msg[3:]

            if msg.upper() == "C":
                waiting_start = False
                waiting_command = True
                isPlaying = 1
                network.sendTo(clients, "The game starts !\n")
                clients[0].send("!>1".encode())
                clients[1].send("!>2".encode())

    send = True
    while waiting_command:
        if send:
            # Once per round, send the map to players
            str = "!.{}".format(maze.getServerMap())
            print(str[2:])
            network.sendTo(clients, "!<{}".format(isPlaying))
            time.sleep(0.3)
            network.sendTo(clients, str)
            time.sleep(0.3)
            network.sendTo(clients, "Player {} is playing !".format(isPlaying))
            send = False

        clients_to_read = []
        clients_to_read, wlist, xlist = select.select(clients, [], [], 0.5)

        for client in clients_to_read:
            msg_received = client.recv(1024)
            msg_received = msg_received.decode()
            # Receive message and execute it
            ret = maze.execute(msg_received, isPlaying)

            if ret != 0:
                if ret == 1:
                    client.send("Your opponent is playing.".encode())
                elif ret == 2:
                    client.send("You can't do that.".encode())
                elif ret == 3:
                    client.send("Unknown command.".encode())
                else:
                    str = "Unknown error : {}".format(ret)
                    client.send(str.encode())
            else:
                if maze.getWinner() != 0:
                    network.sendTo(clients, maze.getServerMap())
                    str = "Player {} has won the game !\n".format(isPlaying)
                    network.sendTo(clients, str)
                    waiting_command = False
                else:
                    isPlaying %= 2
                    isPlaying += 1
                    network.sendTo(clients, "Player {} is playing !\n".format(
                        isPlaying))
                    network.sendTo(clients, "!<{}".format(isPlaying))
                    send = True

    server_started = False

print("Closing server...")
network.sendTo(clients, "!!")
for client in clients:
    client.close()

main_connection.close()
