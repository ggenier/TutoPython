from django.contrib import admin
from .models import Booking, Album, Artist

# Register your models here.
admin.site.register(Booking)
admin.site.register(Artist)
admin.site.register(Album)
