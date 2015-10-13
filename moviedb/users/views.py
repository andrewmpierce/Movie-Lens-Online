from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm
from .models import UserProfile
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from database.models import Rater, Movie, Rating
from database.views import *
from django.contrib.auth.decorators import login_required



# Create your views here.
def rater_register(request):
        return Rater.objects.create(user=request.user,
                            gender=request.POST['gender'],
                            age=request.POST['age'],
                            zipcode=request.POST['zipcode'],
                            occupation=request.POST['occupation'])

def user_register(request):
    form = UserForm(request.POST)
    if form.is_valid():
        user = form.save()
        password = user.password
        user.set_password(password)
        user.save()
        profile = UserProfile(user=user, fav_movie= 'Toy Story')
        profile.save()
        user = authenticate(username=user,
                             password=password)
        user_r = User.objects.get(username=user)
        Rater.objects.create(user=user_r,
                            gender=request.POST['gender'],
                            age=request.POST['age'],
                            zipcode=request.POST['zipcode'],
                            occupation=request.POST['occupation'])
        ratings = []
        try:
            for rating in user_r.rater.rating_set.all():
                ratings.append({'movie':rating.movie,
                                'stars': rating.stars})
        except:
            pass
        login(request, user)
        return render(request,
                    'users/profile_detail.html',
                    {'rater':user_r,
                    'ratings': ratings})
    else:
        form = UserForm()
    return render(request, 'users/register.html',
                  {'form':form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        user_r = User.objects.get(username=username)
        ratings = []
        for rating in user_r.rater.rating_set.all():
            ratings.append({'movie':rating.movie,
                        'stars': rating.stars})
        if user.is_active:
            login(request, user)
            return render(request,
                        'users/userprofile_detail.html',
                        {'rater':user_r,
                        'ratings': ratings})
        else:
            return render(request,
                      'users/login.html',
                      {'failed':True,
                      'username':username})
    return render(request, 'users/login.html')


def user_logout(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        logout(request, user)
    return redirect('database/top_twenty.html')


#@login_required
def view_profile(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    ratings = []
    for rating in rater.rating_set.all():
        ratings.append({'movie':rating.movie,
                    'stars': rating.stars})
    return render(request,
                'users/userprofile_detail.html',
                {'rater':rater,
                'ratings': ratings})


class UserProfileDetail(DetailView):
    model = UserProfile


class UserProfileUpdate(UpdateView):
    model = UserProfile
    fields = ('homepage',)

    def get(self, request, *args, **kwargs):
        return (super(UserProfileUpdate, self).
                get(self, request, *args, **kwargs))
