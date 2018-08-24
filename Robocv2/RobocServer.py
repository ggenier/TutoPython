# -*- coding: utf-8 -*-

import socket
import select


def configurationServer(host='localhost', port=8888):
    # Config de la conenction
    maConnec = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Création de la socket
    maConnec.bind((host, port))
    # On écoute le port
    maConnec.listen(5)

    return maConnec


def envoiMessage(socketAvecClient, messageAEnvoyer):
    socketAvecClient.send(messageAEnvoyer.encode())


def receptionMessage(socketAvecClient):
    message = socketAvecClient.recv(1024)
    message = message.decode()
    print("Message reçu : " + message)
    return message


listeClientsConnectes = list()
connection = configurationServer()
serveurLance = True
listeClientConnu = dict()
premierClientConnu = False

while serveurLance:
    # On vérifie les demandes de connections
    listeConnectionsDemandees, wlist, xlist = select.select([connection], [], [], 0.05)

    # On parcourt les connections a accepter
    for client in listeConnectionsDemandees:
        # On attend un client
        # La liste renvoyé par select.select contient uniquement les nouvelles connections
        socketAvecClient, infoSocketClient = connection.accept()
        listeClientsConnectes.append(socketAvecClient)

    # On attend des messages
    try:
        listeClientALire, wlist, xlist = select.select(listeClientsConnectes, [], [], 0.05)
    except select.error:
        pass
    else:
        # On parcourt les clients à lire
        # La liste contient uniquement ceux qui ont des messages à lire
        for client in listeClientALire:
            # Si on ne connait pas le client, on l'ajoute
            if client.getsockname() not in listeClientConnu:
                listeClientConnu[client.getsockname()] = client

            # Le premier client connecté pourra choisir la map
            if not premierClientConnu:
                premierClientConnu = True
                envoiSelectionMap(client)

connection.close()