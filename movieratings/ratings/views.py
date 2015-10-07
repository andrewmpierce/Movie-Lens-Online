from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Rating, Rater


# Create your views here.
def top_twenty(request):
    movies = Movie.objects.all()
    top_twenty = [str(movies) for movie in sorted(movies, key=movies.id, reverse=True)]
    return HttpResponse('<br>'.join(top_twenty[:20]))
