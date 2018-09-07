from django.db import models

# Create your models here.
# from django.db import models

#Tables
class Artist(models.Model):
    class Meta:
        verbose_name='artiste' #pour affichage dans la console admin , mettre au singulier

    name = models.CharField("nom de l'artiste",max_length=200, unique=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    class Meta:
        verbose_name='prospect'

    email = models.EmailField("email", max_length=100, unique=True)
    name = models.CharField("nom de l'utilisateur", max_length=200)

    def __str__(self):
        return self.name


class Album(models.Model):
    class Meta:
        verbose_name = 'album'

    reference = models.IntegerField("référence de l'album", max_length=200, unique=True)
    created_at = models.DateTimeField("date de création", auto_now_add=True)
    available = models.BooleanField("disponible à la réservation", default=True)
    title = models.CharField("titre de l'album", max_length=200)
    picture = models.URLField("image de la pochette")
    artist = models.ManyToManyField(Artist, related_name='album', blank=True)

    def __str__(self):
        return self.title

class Booking(models.Model):
    class Meta:
        verbose_name = 'réservation'

    created_at = models.DateTimeField("date de création", auto_now_add=True)
    contacted = models.BooleanField("client contacté pour la réservation", default=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    album = models.OneToOneField(Album, on_delete=models.CASCADE,)

    def __str__(self):
        return self.contact.name

