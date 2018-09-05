# -*-coding:Utf-8 -*

"""
This file is the main one

Execute it to start the server
"""

import socket
from threading import Thread

import network

host = "localhost"
port = 12800

player = 0
isPlaying = 0
playing = False
maze = None
t = None


def getFromServ(connection):
    global player, isPlaying, playing, maze

    while playing:
        msg = connection.recv(1024).decode()
        stat, ret = network.getMessage(msg)
        if stat == 0:
            print(ret)
        elif stat == 1:
            player = ret
            playing = True
        elif stat == 2:
            isPlaying = ret
        elif stat == 3:
            print(ret)
        elif stat == 4:
            playing = False


print("Attempt to connect...")
server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_connection.connect((host, port))
print("Connection to the server established.")
playing = True

while playing:
    t = Thread(target=getFromServ, args=(server_connection,))
    t.start()
    msg = input()
    msg = "!{}:{}".format(player, msg)
    server_connection.send(msg.encode())

server_connection.close()
exit()
