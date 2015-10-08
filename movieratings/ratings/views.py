from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Rating, Rater


# Create your views here.
def top_20(request):
    top_twenty = [movie for movie in Movie.objects.all() if type(movie.average_rating()) == float]
    top_twenty = sorted(top_twenty, key = lambda c: c.average_rating(), reverse=True)
    top_twenty = [str(movie) for movie in top_twenty[:20]]
    #return HttpResponse('<br>'.join(top_twenty))
    return render(request,
                  'top_20.html',
                   {'top_twenty':top_twenty})

def show_movies(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    string = ' <center><h3> Title : {} </h3> Average Rating : {}</center>'.format(movie.title, movie.average_rating())
    #return HttpResponse(string)
    return render(request,
                  'movies.html',
                   {'movie':movie})


def users(request, user_id):
    user = Rater.objects.get(pk=user_id)
    string = '<center> <h3> User Id : {} </h3> Age : {} <br> Occupation : {} <br> Gender : {} <br> Zipcode : {}</center>'.format(user.id, user.age, user.occupation, user.gender, user.zipcode)
    #return HttpResponse(string)
    return render(request,
                  'users.html',
                   {'user':user})
