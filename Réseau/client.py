# -*- coding: utf-8 -*-

import socket

maConnec=None

def ouvertureSocket():
    #Config de la conenction
    maConnec = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #On se connect
    maConnec.connect(('localhost', 8888))
    print(maConnec)

    return maConnec

def recevoirMessage(socketAvecServeur):
    message=socketAvecServeur.recv(1024)
    print("Message reçu : "+message.decode())

def envoiMessage(socketAvecServeur):
    message=input("Message a envoyer au serveur : ")
    socketAvecServeur.send(message.encode())
    return message

maConnec = ouvertureSocket()
message = str()
while message != "quitter" and message != 'fin':
    message = envoiMessage(maConnec)
    if message != "quitter" and message != 'fin':
        recevoirMessage(maConnec)

maConnec.close()
