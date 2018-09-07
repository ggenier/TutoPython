from django.contrib import admin
from .models import Booking, Album, Artist, Contact

# Register your models here.

#Sans décorateur
#admin.site.register(Booking)

#Affichage de données liées au contact : les réservations qu'il a effectué
class BookingInline(admin.TabularInline):
    verbose_name = "Réservation"
    verbose_name_plural = "Réservations"
    model = Booking
    fieldsets = [
        (None, {'fields': ['album', 'contacted']})
        ] # list columns
    extra = 0  # Pour ne pas avoir de lignes de saisie sous les albums réservés

#Affichage des albums liés à l'artiste
class AlbumArtistInline(admin.TabularInline):
    verbose_name = "Album"
    verbose_name_plural = "Albums"
    model = Album.artist.through
    extra = 1  # Pour avoir une de saisie sous les albums

#utilisation décorateur
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [BookingInline, ]  # list of bookings made by a contact

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumArtistInline, ]

#Ajout champ de recherche autmatiquement sur le titre des albums dans la console admin
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    search_fields = ['reference', 'title']

#Ajout de filtres sur des booleans
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ['created_at', 'contacted']