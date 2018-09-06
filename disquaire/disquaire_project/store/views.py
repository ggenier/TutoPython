from .models import Album, Artist, Contact, Booking
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
#Version pour HTML simple
# def index(request):
#     albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
#     formatted_albums = ["<li>{} - {}</li>".format(str(album.id), album.title) for album in albums]
#     message = """<u1>{}</u1>""".format("\n".join(formatted_albums))
#     template = loader.get_template('store/index.html')
#     return HttpResponse(template.render(request=request))

#Version pour utilisation gabarit
def index(request):
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    context = {
        'albums': albums
    }

    return render(request, 'store/index.html', context)

#Version pour la version HTML simple
# def listing(request):
#     albums = Album.objects.filter(available=True).order_by('-created_at')
#     formatted_albums = ["<li>{} - {}</li>".format(album.id, album.title) for album in albums]
#     message = """<u1>{}</u1>""".format("\n".join(formatted_albums))
#     return HttpResponse(message)

#Version pour utilisation gabarit
def listing(request):
    albums = Album.objects.filter(available=True).order_by('-created_at')

    paginator = Paginator(albums, 2)
    # Get current page number
    page = request.GET.get('page')
    # Return only this page albums and not others
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        albums = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        albums = paginator.page(paginator.num_pages)

    context = {
        'albums': albums,
        'paginate' : True
    }
    return render(request, 'store/listing.html', context)

#Version pour HTML simple
# def detail(request, album_id):
#     album = Album.objects.get(pk=album_id)
#     artists = " ".join(
#         [artist.name for artist in album.artist.all()])  # grab artists name and create a string out of it.
#     message = "Le nom de l'album est {}. Il a été écrit par {}".format(album.title, artists)
#     return HttpResponse(message)

#Version pour utilisation template
def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    artists = [artist.name for artist in album.artist.all()]
    artists_name = " ".join(artists)
    context = {
        'album_title': album.title,
        'artists_name': artists_name,
        'album_id': album.id,
        'thumbnail': album.picture
    }

    return render(request, 'store/detail.html', context)

def search(request):
    obj = str(request.GET)
    query = request.GET['query']
    if not query:
        message = listing()
    else:
        albums = Album.objects.filter(title__icontains=query)

        if albums.exists():
            albums = Album.objects.filter(artist__name__icontains=query)

    title = "Résultats pour la requête %s" % query
    context = {
        'albums': albums,
        'title': title
    }

    return render(request, 'store/search.html', context)
