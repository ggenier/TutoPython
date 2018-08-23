# -*- coding: utf-8 -*-

import socket
import select

def lancementServeur():
    #Config de la conenction
    maConnec = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Création de la socket
    maConnec.bind(('localhost', 8888))
    #On écoute le port
    maConnec.listen(5)

    return maConnec

def envoiMessage(socketAvecClient, messageAEnvoyer):
    socketAvecClient.send(messageAEnvoyer.encode())

def receptionMessage(socketAvecClient):
    message=socketAvecClient.recv(1024)
    message=message.decode()
    print("Message reçu : "+message)
    return message


listeClientsConnectes = list()
connection = lancementServeur()
serveurLance = True
listeClientConnu = dict()

while serveurLance:
    #On vérifie les demandes de connections
    listeConnectionsDemandees, wlist, xlist = select.select([connection], [], [], 0.05)

    #On parcourt les connections a accepter
    for client in listeConnectionsDemandees:
        # On attend un client
        #La liste renvoyé par select.select contient uniquement les nouvelles connections
        print("On parcourt les demandes de connections")
        socketAvecClient, infoSocketClient = connection.accept()
        listeClientsConnectes.append(socketAvecClient)

    #On attend des messages
    try:
        listeClientALire, wlist, xlist = select.select(listeClientsConnectes, [], [], 0.05)
    except select.error:
        pass
    else:
        #On parcourt les clients à lire
        #La liste contient uniquement ceux qui ont des messages à lire
        for client in listeClientALire:
            print("On parcourt les clients à lire")
            #Si on ne ocnnait pas le client, on l'ajoute
            if client.getsockname() not in listeClientConnu:
                listeClientConnu[client.getsockname()] = client

            message=receptionMessage(client)
            if message == "quitter":
                del(listeClientConnu[client.getsockname()])
                client.close()
                listeClientsConnectes.remove(client)
            else:
                if message == "fin":
                    serveurLance = False
                else:
                    envoiMessage(client, "5 / 5")


connection.close()