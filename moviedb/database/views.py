from django.shortcuts import render
from django.db.models import Avg, Count
from .models import Movie, Rater, Rating
# Create your views here.

def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request,
                  'database/movie_detail.html',
                  {'movie':movie})

def rater_detail(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    ratings = []
    for rating in rater.rating_set.all():
        ratings.append({'movie':rating.movie,
                        'stars': rating.stars})
    return render(request,
                  'database/rater_detail.html',
                  {'rater': rater,
                  'ratings': ratings})


def top_movies(request):
    popular_movies = Movie.objects.annotate(num_ratings=Count('rating')) \
                                  .filter(num_ratings__gte=50)

    movies = popular_movies.annotate(Avg('rating__stars')) \
                           .order_by('-rating__stars__avg')[:20]

    return render(request,
                  'database/top_twenty.html',
                  {'movies': movies})
