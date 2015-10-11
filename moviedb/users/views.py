from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm
from database import views
from .models import UserProfile
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User



# Create your views here.
def user_register(request):
    form = UserForm(request.POST)
    if form.is_valid():
        user = form.save()
        password = user.password
        user.set_password(password)
        user.save()

        profile = UserProfile(user=user, fav_movie= 'Toy Story')
        profile.save()

        user = authenticate(username=user.username,
                            password=password)

        login(request, user)
        view_profile()

    else:
        form = UserForm()
    return render(request, 'users/register.html',
                  {'form':form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        profile = User.objects.get(username=username)
        if user.is_active:
            login(request, user)
            return redirect(reverse('profile_detail', args=[profile.pk]))
        else:
            return render(request,
                      'users/login.html',
                      {'failed':True,
                      'username':username})
    return render(request, 'users/login.html')



class UserProfileDetail(DetailView):
    model = UserProfile


class UserProfileUpdate(UpdateView):
    model = UserProfile
    fields = ('homepage',)

    def get(self, request, *args, **kwargs):
        return (super(UserProfileUpdate, self).
                get(self, request, *args, **kwargs))
