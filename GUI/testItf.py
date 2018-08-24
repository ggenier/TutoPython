# -*-coding:Latin-1 -*

"""Tests des widgets de base"""

from tkinter import *

fenetre = Tk()
var_case = IntVar()
var_texte = StringVar()
var_choix = StringVar()


def champModifie(*args):
    #for arg in args:
    #    print(arg)

    print(var_texte.get())
    print(var_case.get())
    print(var_choix.get())



fenetre.title("Nom fenetre")
label=Label(fenetre, text="Hello World !")
label.pack()

#Champ de saisie
var_texte.trace("w", champModifie)
ligne_texte = Entry(fenetre, textvariable=var_texte, width=30)
ligne_texte.pack()

#Case à cocher
var_case.trace("w", champModifie)
case = Checkbutton(fenetre, text="Ne plus poser cette question", variable=var_case)
case.pack()

#Bouton radio
var_choix.trace("w", champModifie)
choix_rouge = Radiobutton(fenetre, text="Rouge", variable=var_choix, value="rouge",)
choix_vert = Radiobutton(fenetre, text="Vert", variable=var_choix, value="vert")
choix_bleu = Radiobutton(fenetre, text="Bleu", variable=var_choix, value="bleu")

choix_rouge.pack()
choix_vert.pack()
choix_bleu.pack()

#Un cadre pour les liste box
cadreListBox = LabelFrame(fenetre, text="Ma liste de choix")
cadreListBox.pack()
#Liste box
listeBox = Listbox(cadreListBox)
listeBox.pack()
listeBox.insert(END, "Carte")
listeBox.insert(END, "Paypal")

#Cadre
cadre = Frame(fenetre, width=768, height=576, borderwidth=1)
cadre.pack(fill=BOTH)

message = Label(cadre, text="Notre fenêtre")
message.pack(side="top", fill=X)

#Bouton quitter
bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack

fenetre.mainloop()

