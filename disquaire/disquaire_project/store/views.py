from django.http import HttpResponse
from .models import Album, Artist, Contact, Booking

# Create your views here.
def index(request):
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    formatted_albums = ["<li>{} - {}</li>".format(str(album.id), album.title) for album in albums]
    message = """<u1>{}</u1>""".format("\n".join(formatted_albums))
    return HttpResponse(message)

def listing(request):
    albums = Album.objects.filter(available=True).order_by('-created_at')
    formatted_albums = ["<li>{} - {}</li>".format(album.id, album.title) for album in albums]
    message = """<u1>{}</u1>""".format("\n".join(formatted_albums))
    return HttpResponse(message)


def detail(request, album_id):
    album = Album.objects.get(pk=album_id)
    artists = " ".join(
        [artist.name for artist in album.artist.all()])  # grab artists name and create a string out of it.
    message = "Le nom de l'album est {}. Il a été écrit par {}".format(album.title, artists)
    return HttpResponse(message)

def search(request):
    obj = str(request.GET)
    query = request.GET['query']
    if not query:
        message = listing()
    else:
        albums = Album.objects.filter(title__icontains=query)

        if albums.exists():
            albums = Album.objects.filter(artists__name__icontains=query)

        if albums.exists():
            message = "On a vraiment rien trouvé"
        else:
            albums = ["<li>{}</li>".format(album.title) for album in albums]
            message = """
                Nous avons trouvé les albums correspondant à votre requête ! Les voici :
                <ul>
                    {}
                </ul>
            """.format("</li><li>".join(albums))

    return HttpResponse(message)
