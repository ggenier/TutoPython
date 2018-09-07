
#Un formulaire est représenté sous la forme d'une classe, c'est une super idée :)
#Chaque attrcbut de la classe est un chhamp, et les types sont les mêmes que pour les modèles.
#On hérite alors des contrôles automatique
#C'est le fonctionnement de base
#Si notre formlaire contient exactement les champs d'une table, on peut utiliser la solution en dessous

# from django.forms import form
# class ContactForm(forms.Form):
#     """Formulaire de réservation"""
#     name = forms.CharField(label="Nom" #Label affiché à gauche de la zone de saisie
#                            , max_length=100 #Taille max
#                            , widget=forms.TextInput(attrs={'class' : 'form-control'}) #ZOne de saisie
#                            , required=True #Obligatoire
#                            )
#
#     email = forms.EmailField(label="Email" #Label affiché à gauche de la zone de saisie
#                            , max_length=100 #Taille max
#                            , widget=forms.EmailInput(attrs={'class' : 'form-control'}) #ZOne de saisie
#                            , required=True #Obligatoire
#                          )


#Solution si le formulaire contient exactement les champs d'une table
from django.forms import ModelForm, TextInput, EmailInput
from .models import Contact
from django.forms.utils import ErrorList

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email"]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'})
        }

#Pour modifier les erreurs, ici, on change la liste à puce par des paragraphes
class ParagraphErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<p class="small error">%s</p>' % e for e in self])