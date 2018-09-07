from django import forms

#Un formulaire est représenté sous la forme d'une classe, c'est une super idée :)
#Chaque attrcbut de la classe est un chhamp, et les types sont les mêmes que pour les modèles.
#On hérite alors des contrôles automatique

class ContactForm(forms.Form):
    """Formulaire de réservation"""
    name = forms.CharField(label="Nom" #Label affiché à gauche de la zone de saisie
                           , max_length=100 #Taille max
                           , widget=forms.TextInput(attrs={'class' : 'form-control'}) #ZOne de saisie
                           , required=True #Obligatoire
                           )

    email = forms.EmailField(label="Email" #Label affiché à gauche de la zone de saisie
                           , max_length=100 #Taille max
                           , widget=forms.EmailInput(attrs={'class' : 'form-control'}) #ZOne de saisie
                           , required=True #Obligatoire
                         )

