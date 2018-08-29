# -*- coding: utf-8 -*-

import socket
import select
import utils.fonctions
import utils.affichage
from Joueur import Joueur
from labyrinthe.Carte import Carte
import time

listeClientsConnectes = list()
serveurLance = True
listeClientConnu = dict()
mapChoisie = False
premierClient = None #Premier client connecté
partieFinie = False
partieCommence=False

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
    print("Envoi message : "+messageAEnvoyer)
    socketAvecClient.send(messageAEnvoyer.encode())
    time.sleep(0.1)


def receptionMessage(socketAvecClient):
    """Réception du message"""
    message = socketAvecClient.recv(1024)
    message = message.decode()
    print("Message reçu : "+message)
    return message

def joueurDoitJouer(client):
    """On recherche si le joueur doit jouer ou pas"""
    joueurDoitJouer = False

    #On parcourt la liste des client
    for clientACtrl in listeClientConnu:
        joueur = listeClientConnu[clientACtrl]
        #On cherche le premier joueur qui n'a pas joué
        if not joueur.getAJouer():
            break

    joueur2 = listeClientConnu[client]
    #si le premier joueur qui n'a pas joué et le même que celui qui nous envoie le message
    #On autorise le mouvement
    if joueur == joueur2:
        joueurDoitJouer = True

    return joueurDoitJouer

#Sélection de la map avant le lancement du serveur
carteSelectionnee = utils.affichage.affichageListeCarteEtSaisie()

#Sélection de la carte
carte = Carte("maps/" + carteSelectionnee + ".txt")
carte.analyseCarte()
mapChoisie = True

connection = configurationServer()
print("Lancement du server, attente de connection client")
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
                if partieCommence:
                    envoiMessage(client, "PCO") #Partie déjà commencé, impossible de rejoindre
                else:
                    if client not in listeClientConnu:
                        pseudo = utils.fonctions.decomposeMessageAction(messageRecu)
                        print("\tAjout d'un joueur {}".format(pseudo))
                        joueur = Joueur(pseudo, utils.fonctions.choisirLettreJoueur(), client, len(listeClientConnu)+1)
                        # Envoi de la position de joueur dans le tour
                        envoiMessage(client, "POS" + str(joueur.getRepresentation()) + str(joueur.getPositionJeu()))

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

                        if premierClient == None:
                            premierClient = client
                            envoiMessage(client, "SAI")

                        # Si on ne connait pas le client, on l'ajoute
                        if client not in listeClientConnu:
                            listeClientConnu[client] = joueur

            #Début de partie
            if action == "DEB":
                print("\tDébut de partie")
                partieCommence=True
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
                demandeJouerEnvoyee = False
                for clientAEnvoyer in listeClientConnu:
                    joueur = listeClientConnu[clientAEnvoyer]
                    #Si le joueur n'a pas joué
                    if not joueur.getAJouer() and not demandeJouerEnvoyee:
                        demandeJouerEnvoyee = True
                        envoiMessage(clientAEnvoyer, "ACT")
                        tousLesJoueursOntJoue = False
                        #break
                    else:
                        envoiMessage(clientAEnvoyer, "ATT")

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

                #On contrôle que c'est bien à ce joueur de joueur
                if joueurDoitJouer(client):
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
                else:
                    envoiMessage(client, "PJO") #Ce n'est pas au joueur de jouer

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

            if action == "MSG":
                token = suiteAction.split("@")
                pseudoEnvoi = token[0]
                pseudoDestinataire = token[1]
                message = token[2]

                #On cherche le destinataire dans la liste, et envoit le message
                for client in listeClientConnu:
                    joueur = listeClientConnu[client]
                    if joueur.getPseudo() == pseudoDestinataire:
                        envoiMessage(client, "MSG"+pseudoEnvoi+"@"+message)
                        break

connection.close()