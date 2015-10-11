from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm

# Create your views here.
def user_register(request):
    form = UserForm(request.POST)
    if form.is_valid():
        user = form.save()
        password = user.password
        user.set_password(password)
        user.save()

        profile = Profile(user=user, fav_movie= 'Toy Story')
        profile.save()

        user = authenticate(username=user.username,
                            password=password)

        login(request, user)
        return redirect('profile')
    else:
        form = UserForm()
    return render(request, 'users/register.html',
                  {'form':form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user.is_active:
            login(request, user)
            return redirect('profile')
        else:
            return render(request,
                      'users/login.html',
                      {'failed':True,
                      'username':username})
    return render(request, 'users/login.html')
