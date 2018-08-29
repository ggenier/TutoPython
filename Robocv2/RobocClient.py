# -*- coding: utf-8 -*-

import socket
import utils.fonctions
import utils.affichage
from Joueur import Joueur
from labyrinthe.Carte import Carte

maConnec=None
carte=None
mapSelect=None
partieFinie = False

def ouvertureSocket(machineDistante='localhost', port=8888):
    #Config de la conenction
    print("On tente de se connecter au serveur...")
    maConnec = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #On se connect
    print("Connexion établie avec le serveur.")
    maConnec.connect((machineDistante, port))

    return maConnec

def recevoirMessage():
    message=maConnec.recv(1024)
    message=message.decode()
    #print("Message reçu : "+message)
    return message

def envoiMessage(message):
    maConnec.send(message.encode())

pseudo=input("Saisir votre pseudo : ")
maConnec = ouvertureSocket()
message = str()
estConnecte=False
joueur = None

while message != "quitter" and message != 'fin':

    if not estConnecte:
        #On envoit la demande de création du joueur
        envoiMessage("ADD" + pseudo)
        joueur = Joueur(pseudo, "", maConnec, 0)
        estConnecte = True

    message=recevoirMessage()

    if message is not None:
        action = utils.fonctions.actionAEffectuer(message)
        suite_action = utils.fonctions.decomposeMessageAction(message)

        #Saisie de la carte à jouer
        if action == "SAI":
            action=input("Taper sur entrer pour commencer la partie.")
            #On reste bloqué t'en qu'on a pas taper sur entré
            envoiMessage("DEB")

        #Mise en place du joueur sur la carte
        if action == 'POS':
            joueur.setPositionJeu(suite_action[1])
            joueur.setRepresentation(suite_action[0])
            print("Vous êtes le joueur n°{}. Vous êtes la lettre {} sur la carte.".format(suite_action[1], joueur.getRepresentation()))

        #Fin de la partie
        if action == 'FIN':
            partieFinie = True
            lettre = suite_action[0]
            pseudo = suite_action[1:len(suite_action)]
            if joueur.getRepresentation() == lettre:
                print("Bravo vous avez gagné en {} coups.".format(len(joueur.getHisto())))
            else:
                print("Désolé vous avez perdu. {} alias {} a été le plus fort cette fois.".format(lettre, pseudo))

        #Affichage d'un message d'information
        if action == 'INF':
            print("INF"+suite_action)

        #Retour du serveur suite à la map sélectionnée
        if action == "MAP":
            mapSelect = suite_action
            if suite_action[0] == "_":
                mapSelect = suite_action[1:len(suite_action)]

            print("Carte sélectionnée {}".format(mapSelect))

            #Action diférente si les autres joueurs sont déjà connectés
            #if suite_action[0] == "_":
                #print("En attente du lancement de la partie...")

            #Chargement de la carte
            if carte is None:
                carte = Carte("maps/"+mapSelect+".txt")
                carte.analyseCarte()

            print("La partie n'a pas commencé. Veuillez patienter")

        #Sasiie d'une action, déplacement, création d'un mur...
        if action == "ACT":
            #Chargement de la carte
            if carte is None:
                carte = Carte("maps/"+mapSelect+".txt")
                carte.analyseCarte()

            if not partieFinie:
                direction, nbDeplacement = utils.affichage.saisieDeplacement()

                #Déplement du robot
                if str(nbDeplacement).isnumeric():
                    # Controle du déplacement par le serveur
                    #CTR+lettre+direction+deplacement
                    chaine = "CTR"+joueur.getRepresentation()+direction+str(nbDeplacement)

                #Construction d'une porte ou d'un mur
                if str(nbDeplacement) in "mp":
                    if nbDeplacement.lower() == "m":
                        actionAEnvoyer="MUR"

                    if nbDeplacement.lower() == "p":
                        actionAEnvoyer="DEL"

                    chaine = actionAEnvoyer + joueur.getRepresentation() + direction

                envoiMessage(chaine)

        #Déplacement OK
        if action == "DOK":
            representation, pseudo, positions = utils.fonctions.decomposeMessageDeplacement(suite_action)
            joueur.setPosition(positions)
            #CEla propagera le déplacement aux autres clients
            envoiMessage("DEP" + str(joueur.getRepresentation()) + joueur.getPseudo() + str(joueur.getPosition()))

        #Déplacement KO
        if action == "DKO":
            print("Déplacement non autorisé")
            #On va recevoir un ACT pour resaisir

        #On reiniitalise la carte avant le rafraichissement
        if action == 'INI':
            if carte is None:
                # Chargement de la carte
                carte = Carte("maps/" + str(mapSelect) + ".txt")
                carte.analyseCarte()

            #Supprime les joueurs de la structures avant des les rajouter aux nouvelles positions
            carte.viderStructure()

        #On replace chaque joueur
        if action == "DEB":
            representation, pseudo, positions = utils.fonctions.decomposeMessageDeplacement(suite_action)
            joueurTempo = Joueur(pseudo, representation, None, 0)
            joueurTempo.setPosition(positions)
            carte.positionnerJoueur(joueurTempo)

        #Rafracihissement de la carte
        if action == "RAF":
            utils.affichage.affichageStructureCarte(carte.getStructureCarte())

        #Notification du déplacement du joueur
        if action == "DEP":
            if carte is None:
                # Chargement de la carte
                carte = Carte("maps/" + str(mapSelect) + ".txt")
                carte.analyseCarte()

            representation, pseudo, positions = utils.fonctions.decomposeMessageDeplacement(suite_action)
            joueurTempo = Joueur(pseudo, representation, None, 0)
            joueurTempo.setPosition(positions)
            carte.positionnerJoueur(joueurTempo)

            #Déplacement d'un joueur, rafraichissement de l'écran
            #utils.affichage.affichageStructureCarte(carte.getStructureCarte())
            #print("En attente des autres joueurs")

        #Ajout d'un mur aux positions indiquées
        if action == "MUR":
            suite_action = suite_action.replace("(", "")
            suite_action = suite_action.replace(")", "")
            suite_action = suite_action.split(",")

            carte.setObstacle(None, "O", (int(suite_action[0]), int(suite_action[1]), int(suite_action[2])))
            utils.affichage.affichageStructureCarte(carte.getStructureCarte())

        #Ajout d'un mur aux positions indiquées
        if action == "DEL":
            print("tt " +suite_action)
            suite_action = suite_action.replace("(", "")
            suite_action = suite_action.replace(")", "")
            suite_action = suite_action.split(",")

            carte.setObstacle(None, ".", (int(suite_action[0]), int(suite_action[1]), int(suite_action[2])))
            utils.affichage.affichageStructureCarte(carte.getStructureCarte())

        if action == "CKO":
            print("Création d'un mur impossible ici.")

        if action == "SKO":
            print("Suppression d'un mur impossible ici.")

maConnec.close()
