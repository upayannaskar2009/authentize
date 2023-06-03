from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'index.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return render(request, 'index.html', {'name' : username})
        else:
            messages.error(request, 'No such user, make sure you entered the details correctly')
    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        new_user = User.objects.create_user(username, email, pass1)
        new_user.save()
        return redirect('signin')

    return render(request, 'signup.html')

def signout(request):
    logout(request)
    messages.success(request, 'Logged Out')
    return redirect('/')