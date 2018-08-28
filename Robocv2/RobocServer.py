# -*- coding: utf-8 -*-

import socket
import select
import utils.fonctions
from Joueur import Joueur
from labyrinthe.Carte import Carte
import time

listeClientsConnectes = list()
serveurLance = True
listeClientConnu = dict()
mapChoisie = False
premierClient = None #Premier client connecté
partieFinie = False

def configurationServer(host='localhost', port=8888):
    """Configuration du serveur"""
    # Config de la connection
    maConnec = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Création de la socket
    maConnec.bind((host, port))
    # On écoute le port
    maConnec.listen(5)

    return maConnec


def envoiMessage(socketAvecClient, messageAEnvoyer):
    """Envoi d'un mesasge vers le client"""
    #print("Envoi message : "+messageAEnvoyer)
    socketAvecClient.send(messageAEnvoyer.encode())
    time.sleep(0.1)


def receptionMessage(socketAvecClient):
    """Réception du message"""
    message = socketAvecClient.recv(1024)
    message = message.decode()
    return message


connection = configurationServer()
print("Lancment du server, attente de connection client")
while serveurLance:
    # On vérifie les demandes de connections
    listeConnectionsDemandees, wlist, xlist = select.select([connection], [], [], 0.05)

    # On parcourt les connections a accepter
    for client in listeConnectionsDemandees:
        print("\tDemande de connection")
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
            messageRecu = receptionMessage(client)
            action = utils.fonctions.actionAEffectuer(messageRecu)
            suiteAction = utils.fonctions.decomposeMessageAction(messageRecu)

            #Création du joueur
            if action == "ADD":
                if client not in listeClientConnu:
                    pseudo = utils.fonctions.decomposeMessageAction(messageRecu)
                    print("\tAjout d'un joueur {}".format(pseudo))
                    joueur = Joueur(pseudo, utils.fonctions.choisirLettreJoueur(), client, len(listeClientConnu)+1)
                    # Envoi de la position de joueur dans le tour
                    envoiMessage(client, "POS" + str(joueur.getRepresentation()) + str(joueur.getPositionJeu()))

                    #Le premier client choisi la map
                    if len(listeClientConnu) == 0 and not mapChoisie:
                        print("\tDemande de sélection de la map")
                        envoiMessage(client, "SAI")#saisie de la map
                        premierClient = client

                    if mapChoisie:
                        print("\tEnvoi de la carte sélectionné au client qui vient de se connecter")
                        envoiMessage(client, "MAP"+carteSelectionnee)
                        #On positionne les joueurs déjà connectés
                        trouve, etage, ligne, colonne = carte.rechercheEmplacementLibre()
                        # Debut de partie, on déplace le joueur
                        joueur.setPosition((etage, ligne, colonne))
                        NouvelObstacle = carte.getObstacle(joueur.getPosition())
                        obstacleARemettre = joueur.getObjetPrecedent()
                        joueur.setObjetPrecedent(NouvelObstacle)
                        carte.positionnerJoueur(joueur)
                        listeClientConnu[client] = joueur

                    # Si on ne connait pas le client, on l'ajoute
                    if client not in listeClientConnu:
                        listeClientConnu[client] = joueur

            #Sélection de la map
            if action == "MAP":
                print("\tRetour map sélectionnée")
                #Retour de la map sélectionnée
                #Création de la map
                carteSelectionnee = utils.fonctions.decomposeMessageAction(messageRecu)
                #On crée la carte
                carte = Carte("maps/"+carteSelectionnee+".txt")
                carte.analyseCarte()

                #On informe les autres joueurs que la carte est sélectionné et on les place
                print("\tEnvoi de la map sélectionnée aux clients connectés")
                for clientEnvoi in listeClientConnu:
                    if clientEnvoi is not premierClient:
                        envoiMessage(clientEnvoi, "MAP_" + carteSelectionnee)

                for clientEnvoi in listeClientConnu:
                    joueur = listeClientConnu[clientEnvoi]
                    #On positionne les joueurs déjà connectés
                    trouve, etage, ligne, colonne = carte.rechercheEmplacementLibre()
                    # Debut de partie, on déplace le joueur
                    joueur.setPosition((etage, ligne, colonne))
                    NouvelObstacle = carte.getObstacle(joueur.getPosition())
                    obstacleARemettre = joueur.getObjetPrecedent()
                    joueur.setObjetPrecedent(NouvelObstacle)
                    carte.positionnerJoueur(joueur)
                    listeClientConnu[clientEnvoi] = joueur

                mapChoisie=True

            #Début de partie
            if action == "DEB":
                print("\tDébut de partie")
                #Chaque joueur va positionner les autres joueurs, lui inclus
                for clientEnvoi in listeClientConnu:
                    envoiMessage(clientEnvoi, "INI")  # Init de la carte

                for clientEnvoi in listeClientConnu:
                    joueur = listeClientConnu[clientEnvoi]
                    chaine = "DEB" + str(joueur.getRepresentation()) + str(joueur.getPseudo()) + str(
                        joueur.getPosition())

                    for clientEnvoiParcours2 in listeClientConnu:
                        envoiMessage(clientEnvoiParcours2, chaine)

                for clientEnvoi in listeClientConnu:
                    #Rafraichissement de l'écran
                    envoiMessage(clientEnvoi, "RAF")

                #On envoit la demande de déplacement
                tousLesJoueursOntJoue = True
                for clientAEnvoyer in listeClientConnu:
                    joueur = listeClientConnu[clientAEnvoyer]
                    #Si le joueur n'a pas joué
                    if not joueur.getAJouer():
                        envoiMessage(clientAEnvoyer, "ACT")
                        tousLesJoueursOntJoue = False
                        break

                if tousLesJoueursOntJoue:
                    for clientAEnvoyer in listeClientConnu:
                        joueur = listeClientConnu[clientAEnvoyer]
                        joueur.setAJouer(False)
                        listeClientConnu[clientAEnvoyer] = joueur

            #Déplacement du joueur
            if action == "DEP":
                #La déplacement a été approuvé par le client
                representation, pseudo, positions  = utils.fonctions.decomposeMessageDeplacement(suiteAction)
                print("\tDéplacement joueur {} aux positions {} {} {}".format(representation, positions[0], positions[1], positions[2]))

                #Reinit de la carte chez les clients
                for clientEnvoi in listeClientConnu:
                    envoiMessage(clientEnvoi, "INI")  # Init de la carte

                for clientEnvoi in listeClientConnu:
                    joueur = listeClientConnu[clientEnvoi]
                    chaine = "DEP"+str(joueur.getRepresentation())+joueur.getPseudo()+str(joueur.getPosition())
                    # Chaque joueur va positionner les autres joueurs
                    for clientEnvoiParcours2 in listeClientConnu:
                        #Envoi des positions des joueurs, structrure Xpseudo(0,0,0)
                        envoiMessage(clientEnvoiParcours2, chaine)

                for clientEnvoi in listeClientConnu:
                    envoiMessage(clientEnvoi, "RAF")  # Init de la carte

                # On indique que le joueur à jouer
                joueur = listeClientConnu[client]
                joueur.setAJouer(True)
                listeClientConnu[client] = joueur

                #Si la partie est finie, on ne demande plus d'action
                if partieFinie:
                    #Envoi du message à tous les clients
                    for clientAEnvoyer in listeClientConnu:
                        envoiMessage(clientAEnvoyer,
                                     "FIN" + joueur.getRepresentation() + joueur.getPseudo())
                else:
                    #On envoit la demande de déplacement
                    tousLesJoueursOntJoue = True
                    for clientAEnvoyer in listeClientConnu:
                        joueur = listeClientConnu[clientAEnvoyer]
                        #Si le joueur n'a pas joué
                        if not joueur.getAJouer():
                            envoiMessage(clientAEnvoyer, "ACT")
                            tousLesJoueursOntJoue = False
                            break

                    if tousLesJoueursOntJoue:
                        for clientAEnvoyer in listeClientConnu:
                            joueur = listeClientConnu[clientAEnvoyer]
                            joueur.setAJouer(False)
                            listeClientConnu[clientAEnvoyer] = joueur

                        #On refait jouer le premier
                        for clientAEnvoyer in listeClientConnu:
                            envoiMessage(clientAEnvoyer, "ACT")
                            break

            #Controle du déplacement du joueur
            if action == "CTR":
                suiteMessage = utils.fonctions.decomposeMessageAction(messageRecu)

                lettre = suiteMessage[0]
                direction = suiteMessage[1]
                nbDeplacement = int(suiteMessage[2:len(suiteMessage)])
                joueur = listeClientConnu[client]

                deplacementAutorise, partieFinie, etage, ligne, colonne = carte.deplacementAutorise(joueur.getPosition(), direction, nbDeplacement)

                joueur.setPosition((etage, ligne, colonne))
                # On sauvegarde l'ancien objet si non nul
                NouvelObstacle = carte.getObstacle(joueur.getPosition())
                # On récupère l'ancien objet du joueur
                obstacleARemettre = joueur.getObjetPrecedent()
                joueur.setObjetPrecedent(NouvelObstacle)
                carte.setObstacle(obstacleARemettre)
                carte.positionnerJoueur(joueur)
                listeClientConnu[client] = joueur

                #on indique que le déplacement est OK, et on re recevra un message de déplacement à propager
                envoiMessage(client, "DOK"+joueur.getRepresentation()+joueur.getPseudo()+str(joueur.getPosition()))

            if action == "MUR":
                #Création d'un mur
                representation, direction = utils.fonctions.decomposeMessageObstacle(suiteAction)
                joueur = listeClientConnu[client]
                print("\tCreation mur {} {}".format(direction, joueur.getPosition()))
                creationPossible, positions = carte.creationObstacle("O", direction, joueur.getPosition())
                if not creationPossible:
                    #CReation impossible à l'endroit demandé
                    envoiMessage(client, "CKO")
                    envoiMessage(client, "ACT")
                else:
                    joueur = listeClientConnu[client]
                    joueur.setAJouer(True)
                    listeClientConnu[client] = joueur

                    #On envoit la creation du mur aux clients pour rafraichissement
                    for clientAEnvoyer in listeClientConnu:
                        envoiMessage(clientAEnvoyer, "MUR"+str(positions))

                    # On envoit la demande de déplacement
                    tousLesJoueursOntJoue = True
                    for clientAEnvoyer in listeClientConnu:
                        joueur = listeClientConnu[clientAEnvoyer]
                        # Si le joueur n'a pas joué
                        if not joueur.getAJouer():
                            envoiMessage(clientAEnvoyer, "ACT")
                            tousLesJoueursOntJoue = False
                            break

                    if tousLesJoueursOntJoue:
                        for clientAEnvoyer in listeClientConnu:
                            joueur = listeClientConnu[clientAEnvoyer]
                            joueur.setAJouer(False)
                            listeClientConnu[clientAEnvoyer] = joueur

                        # On refait jouer le premier
                        for clientAEnvoyer in listeClientConnu:
                            envoiMessage(clientAEnvoyer, "ACT")
                            break

            if action == "DEL":
                # Suppresson d'un mur
                print("\tSuppression mur")
                representation, direction = utils.fonctions.decomposeMessageObstacle(suiteAction)
                joueur = listeClientConnu[client]
                suppressionPossible, positions = carte.creationObstacle(".", direction, joueur.getPosition())

                if not suppressionPossible:
                    #Suppression impossible ici
                    envoiMessage(client, "SKO")
                    envoiMessage(client, "ACT")
                else:
                    joueur = listeClientConnu[client]
                    joueur.setAJouer(True)
                    listeClientConnu[client] = joueur
                    #On envoit la suppression du mur aux clients pour rafraichissement
                    for clientAEnvoyer in listeClientConnu:
                        envoiMessage(clientAEnvoyer, "DEL"+str(positions))

                    # On envoit la demande de déplacement
                    tousLesJoueursOntJoue = True
                    for clientAEnvoyer in listeClientConnu:
                        joueur = listeClientConnu[clientAEnvoyer]
                        # Si le joueur n'a pas joué
                        if not joueur.getAJouer():
                            envoiMessage(clientAEnvoyer, "ACT")
                            tousLesJoueursOntJoue = False
                            break

                    if tousLesJoueursOntJoue:
                        for clientAEnvoyer in listeClientConnu:
                            joueur = listeClientConnu[clientAEnvoyer]
                            joueur.setAJouer(False)
                            listeClientConnu[clientAEnvoyer] = joueur

                        # On refait jouer le premier
                        for clientAEnvoyer in listeClientConnu:
                            envoiMessage(clientAEnvoyer, "ACT")
                            break

            if action == "QUI":
                serveurLance = False

connection.close()