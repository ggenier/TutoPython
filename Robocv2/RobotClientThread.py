# -*- coding: utf-8 -*-

import socket
import utils.fonctions
import utils.affichage
from Joueur import Joueur
from labyrinthe.Carte import Carte
from threading import Thread, RLock
import sys


verrou = RLock()

class Connection():
   
    def __init__(self, machineDistante='localhost', port=8888):
        self.machineDistante = machineDistante
        self.port = port
        self.maConnec = None
        self.ouvertureSocket()
        
    def ouvertureSocket(self):
        # Config de la conenction
        print("On tente de se connecter au serveur...")
        self.maConnec = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # On se connect
        print("Connexion établie avec le serveur.")
        self.maConnec.connect((self.machineDistante, self.port))

    def recevoirMesage(self):
        message = self.maConnec.recv(1024)
        message = message.decode()
        #print("Message reçu : " + message)
        return message

    def envoiMessage(self, message):
        #print("Envoi message : "+message)
        self.maConnec.send(message.encode())

    def fermertureConnection(self):
        self.maConnec.close()


class RobotEcoute(Thread):
    def __init__(self, connection, pseudo, robotjeu):
        Thread.__init__(self)
        self.connection = connection
        self.pseudo = pseudo
        self.robotjeu = robotjeu

    def run(self):
        message=str()
        while message != 'quitter':
            message = self.connection.recevoirMesage()
            if len(message) > 0:
                #print("Trait : "+message)
                self.robotjeu.traitementMessage(message)
                message=str()

class RobotEcrit(Thread):
    def __init__(self, connection, pseudo):
        Thread.__init__(self)
        self.connection = connection
        self.pseudo = pseudo
        self.message = str()
        self.joueur = None
        self.estConnecte = False
        self.partieCommencee = False

    def setPartieCommencee(self):
        self.partieCommencee = True

    def setJoueur(self, joueur):
        self.joueur = joueur

    def setEstConnecte(self):
        self.estConnecte = True

    def envoiMessage(self, message):
        """Envoi directement le message"""
        with verrou:
            self.connection.envoiMessage(message)

    def run(self):
        while self.message != 'quitter':
            if self.estConnecte:
                if len(self.message) == 0:
                    message = input("")
                    if len(message) == 0:
                        print("Saisir une commande ou @pseudo <message> pour envoyer un message")
                    else:
                        # On a saise un message
                        if str(message).startswith("@"):
                            message = message.replace(" ", "@", 1)
                            self.message = "MSG" + self.joueur.getPseudo() + message
                        else:
                            if message == "c" and  not self.partieCommencee: #Démarrage de la partie
                                self.message = "DEB"
                                self.partieCommencee = True
                            else:
                                # On a saisie autre chose
                                saisieValide, direction, nombreDeplacement = utils.affichage.controleSaisieDirection(
                                    message)
                                if saisieValide:
                                    if str(nombreDeplacement).isnumeric():
                                        # Controle du déplacement par le serveur
                                        # CTR+lettre+direction+deplacement
                                        chaine = "CTR" + self.joueur.getRepresentation() + direction + str(
                                            nombreDeplacement)

                                    # Construction d'une porte ou d'un mur
                                    if str(nombreDeplacement) in "mp":
                                        if nombreDeplacement.lower() == "m":
                                            actionAEnvoyer = "MUR"

                                        if nombreDeplacement.lower() == "p":
                                            actionAEnvoyer = "DEL"

                                        chaine = actionAEnvoyer + self.joueur.getRepresentation() + direction

                                    self.message = chaine

                if len(self.message) > 0:
                    self.envoiMessage(self.message)
                    self.message=str()


class RobotClientJeu():

    def __init__(self, pseudo):
        self.pseudo = pseudo
        self.carte = None
        self.mapSelect = None
        self.partieFinie = False
        self.robotEcrit = None
        self.message = str()
        self.estConnecte = False
        self.joueur = None

    def setRobotEcrit(self, robotEcrit):
        self.robotEcrit = robotEcrit

    def getJoueur(self):
        return self.joueur

    def traitementMessage(self, message):

        if not self.estConnecte:
            self.robotEcrit.setEstConnecte()
            # On envoit la demande de création du joueur
            self.robotEcrit.envoiMessage("ADD" + self.pseudo)
            self.joueur = Joueur(self.pseudo, "", None, 0)
            self.estConnecte = True

        action = utils.fonctions.actionAEffectuer(message)
        suite_action = utils.fonctions.decomposeMessageAction(message)

        # Mise en place du joueur sur la carte
        if action == 'POS':
            self.joueur.setPositionJeu(suite_action[1])
            self.joueur.setRepresentation(suite_action[0])
            print("Vous êtes le joueur n°{}. Vous êtes la lettre {} sur la carte.".format(suite_action[1],
                                                                                          self.joueur.getRepresentation()))

        # Fin de la partie
        if action == 'FIN':
            self.partieFinie = True
            lettre = suite_action[0]
            pseudo = suite_action[1:len(suite_action)]
            if self.joueur.getRepresentation() == lettre:
                print("Bravo vous avez gagné en {} coups.".format(len(self.joueur.getHisto())))
            else:
                print("Désolé vous avez perdu. {} alias {} a été le plus fort cette fois.".format(lettre, pseudo))

        # Affichage d'un message d'information
        if action == 'INF':
            print("INF" + suite_action)

        # Retour du serveur suite à la map sélectionnée
        if action == "MAP":
            self.mapSelect = suite_action
            if suite_action[0] == "_":
                self.mapSelect = suite_action[1:len(suite_action)]

            print("Carte sélectionnée {}".format(self.mapSelect))

            # Chargement de la carte
            if self.carte is None:
                self.carte = Carte("maps/" + self.mapSelect + ".txt")
                self.carte.analyseCarte()

            print("\nTaper c pour commencer la partie.")

        # Sasiie d'une action, déplacement, création d'un mur...
        if action == "ACT":
            # Chargement de la carte
            if self.carte is None:
                self.carte = Carte("maps/" + self.mapSelect + ".txt")
                self.carte.analyseCarte()

            print("A vous de jouer, symbol ({})".format(self.joueur.getRepresentation()))

        # Déplacement OK
        if action == "DOK":
            representation, self.pseudo, positions = utils.fonctions.decomposeMessageDeplacement(suite_action)
            self.joueur.setPosition(positions)
            # CEla propagera le déplacement aux autres clients
            self.robotEcrit.envoiMessage("DEP" + str(self.joueur.getRepresentation()) + self.joueur.getPseudo() + str(self.joueur.getPosition()))

        # Déplacement KO
        if action == "DKO":
            print("Déplacement non autorisé")
            # On va recevoir un ACT pour resaisir

        # On reiniitalise la carte avant le rafraichissement
        if action == 'INI':
            if self.carte is None:
                # Chargement de la carte
                self.carte = Carte("maps/" + str(self.mapSelect) + ".txt")
                self.carte.analyseCarte()

            # Supprime les joueurs de la structures avant des les rajouter aux nouvelles positions
            self.carte.viderStructure()

        # On replace chaque joueur
        if action == "DEB":
            representation, pseudo, positions = utils.fonctions.decomposeMessageDeplacement(suite_action)
            joueurTempo = Joueur(pseudo, representation, None, 0)
            joueurTempo.setPosition(positions)
            self.carte.positionnerJoueur(joueurTempo)

        # Rafracihissement de la carte
        if action == "RAF":
            utils.affichage.affichageStructureCarte(self.carte.getStructureCarte())

        # Pas son tour
        if action == "PJO":
            print("Ce n'est pas à vous de jouer.")

        # Notification du déplacement du joueur
        if action == "DEP":
            if self.carte is None:
                # Chargement de la carte
                self.carte = Carte("maps/" + str(self.mapSelect) + ".txt")
                self.carte.analyseCarte()

            representation, pseudo, positions = utils.fonctions.decomposeMessageDeplacement(suite_action)
            joueurTempo = Joueur(pseudo, representation, None, 0)
            joueurTempo.setPosition(positions)
            self.carte.positionnerJoueur(joueurTempo)

        # Ajout d'un mur aux positions indiquées
        if action == "MUR":
            suite_action = suite_action.replace("(", "")
            suite_action = suite_action.replace(")", "")
            suite_action = suite_action.split(",")

            self.carte.setObstacle(None, "O", (int(suite_action[0]), int(suite_action[1]), int(suite_action[2])))
            utils.affichage.affichageStructureCarte(self.carte.getStructureCarte())

        # Ajout d'un mur aux positions indiquées
        if action == "DEL":
            suite_action = suite_action.replace("(", "")
            suite_action = suite_action.replace(")", "")
            suite_action = suite_action.split(",")

            self.carte.setObstacle(None, ".", (int(suite_action[0]), int(suite_action[1]), int(suite_action[2])))
            utils.affichage.affichageStructureCarte(self.carte.getStructureCarte())

        if action == "CKO":
            print("Création d'un mur impossible ici.")

        if action == "SKO":
            print("Suppression d'un mur impossible ici.")

        if action == "PCO":
            print("Désolé, la partie a déjà commencée. Essayez de vous reconnecter plus tard")
            exit(0)

        if action == "MSG":
            token=suite_action.split("@")
            pseudo = token[0]
            message = token[1]
            print("@{} > {}".format(pseudo, message))


if __name__ == "__main__":
    pseudo = input("Saisir votre pseudo : ")
    connection = Connection('localhost', 8888)

    jeu = RobotClientJeu(pseudo)
    robotEcrit = RobotEcrit(connection, pseudo)
    jeu.setRobotEcrit(robotEcrit)

    robotEcoute = RobotEcoute(connection, pseudo, jeu)

    robotEcrit.start()
    robotEcoute.start()

    #On lance la connection
    jeu.traitementMessage("")
    #On donne le joueur après connection
    robotEcrit.setJoueur(jeu.getJoueur())

