from django.contrib import admin
from .models import Booking, Album, Artist, Contact
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

#Mixin, lasse pour générer les urls pour créer les liens sur les objets
class AdminURLMixin(object):
    def get_admin_url(self, obj):
        content_type = ContentType.objects.get_for_model(obj.__class__)
        return reverse("admin:store_%s_change" % (
            content_type.model),
            args=(obj.id,))

# Register your models here.

#Sans décorateur
#admin.site.register(Booking)

#Affichage de données liées au contact : les réservations qu'il a effectué
class BookingInline(admin.TabularInline, AdminURLMixin):
    #On ne pourra pas ajouter de réservation
    def has_add_permission(self, request):
        return False

    #Le titre de l'album sera sous forme de lien
    def album_link(self, booking):
        url = self.get_admin_url(booking.album)
        return mark_safe("<a href='{}'>{}</a>".format(url, booking.album.title))

    album_link.short_description = "Album"

    verbose_name = "Réservation"
    verbose_name_plural = "Réservations"
    model = Booking
    fields = ["created_at", "album_link", "contacted"]
    readonly_fields = ["created_at", "contacted", "album_link"]  # Ajout du champ date de création en lecture seule
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
class BookingAdmin(admin.ModelAdmin, AdminURLMixin):
    #On ne pourra pas ajouter de réservation
    def has_add_permission(self, request):
        return False

    #Le titre de l'album sera sous forme de lien
    def album_link(self, booking):
        url = self.get_admin_url(booking.album)
        return mark_safe("<a href='{}'>{}</a>".format(url, booking.album.title))

    def contact_link(self, booking):
        url = self.get_admin_url(booking.contact)
        return mark_safe("<a href='{}'>{}</a>".format(url, booking.contact.name))

    #Description dans le fenêtre d'admin
    album_link.short_description = "Album"
    contact_link.short_description = "Contact"

    fields = ["created_at", "contact_link", 'album_link', 'contacted'] #Champ à afficher
    list_filter = ['created_at', 'contacted']
    #attention à l'ordre, il doit etre le même que celui du formulaire
    readonly_fields = ["created_at", "contact_link", 'album_link', 'contacted'] #Ajout du champ date de création en lecture seule