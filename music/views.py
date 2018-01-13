from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hey this is the Music page</h1>")


def detail(request, album_id):
    return HttpResponse("<h2>Details Page of " + album_id + "</h2>")
