from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=email, password=password)
        user.save()
        print('HERE')

        return redirect('/')

    else:
        return render(request, 'register.html')