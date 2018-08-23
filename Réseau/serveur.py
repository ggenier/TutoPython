# -*- coding: utf-8 -*-

import socket

def ouvertureSocket():
    #Config de la conenction
    maConnec = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Création de la socket
    maConnec.bind(('localhost', 8888))
    #On écoute le port
    maConnec.listen(5)

    #On attend un client
    socketAvecClient, infoSocketClient = maConnec.accept()
    print(infoSocketClient)

    return socketAvecClient

def envoiMessage(socketAvecClient, messageAEnvoyer):
    socketAvecClient.send(messageAEnvoyer.encode())

def receptionMessage(socketAvecClient):
    message=socketAvecClient.recv(1024)
    message=message.decode()
    print("Message reçu : "+message)
    return message


socketAvecClient = ouvertureSocket()

#Tant qu'on a pas reçu fin
while receptionMessage(socketAvecClient) != "fin":
    #On répond
    envoiMessage(socketAvecClient, "5/5")

socketAvecClient.close()
