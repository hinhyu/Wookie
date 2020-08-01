from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile
from django.contrib.auth import get_user_model
# User = get_user_model()

# Create your views here.

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = Profile.objects.create_user(username = request.POST['username'], password=request.POST['password1'])
            user.school = request.POST["school"]
            user.gender = request.POST["gender"]
            user.nickname = request.POST["nickname"]
            user.save()
            auth.login(request,user)
            return redirect('/main')
    return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/login')
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')
    return render(request, 'login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('/main')
    return render(request, 'main.html')