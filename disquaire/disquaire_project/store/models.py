from django.db import models

# Create your models here.
# from django.db import models

#Tables
class Artist(models.Model):
    name = models.CharField(max_length=200, unique=True)

class Contact(models.Model):
    email = models.EmailField("email", max_length=100, unique=True)
    name = models.CharField("nom de l'utilisateur", max_length=200)

class Album(models.Model):
    reference = models.IntegerField("référence de l'album", max_length=200, unique=True)
    created_at = models.DateTimeField("date de création", auto_new_add=True)
    available = models.BooleanField("disponible à la réservation", default=True)
    titre = models.CharField("titre de l'album", max_length=200)
    picture = models.UrlField("image de la pochette")
    artist = models.ManyToManyField(Artist, related_name='album', blank=True)

class Booking(models.Model):
    created_at = models.DateTimeField("date de création", auto_new_add=True)
    contacted = models.BooleanField("client contacté pour la réservation", default=True)
    contact = models.ForeignKey("identifiant contact ayant fait la réservation", Contact)
    album = models.OneToOneField("identifiant album réservé", Album)

class Artiste(models.Model):
    name = models.CharField("nom de l'artiste", max_length=60)

