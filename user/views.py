from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid email or password')
            return redirect('login')

    else:
        return render(request, 'user/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            print('USERNAME')
            messages.info(request, 'Username taken')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            print('EMAIL')
            messages.info(request, 'Email taken')
            return redirect('signup')
        else:
            print('CREATE')
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

        return redirect('/')

    else:
        return render(request, 'user/signup.html')