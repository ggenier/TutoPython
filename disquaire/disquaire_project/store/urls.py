from django.conf.urls import url

from . import views # import views so we can use them in urls.
from django.urls import path

urlpatterns = [
    url(r'^$', views.listing),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail),
    url(r'^search/$', views.search)
]