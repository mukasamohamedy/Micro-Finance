from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages 
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        username = request.POST['username']
        phonenumber = request.POST['phonenumber']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('register')
            elif User.objects.filter(phone_no=phonenumber).exists():
                messages.info(request, 'Phone number already used')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    phone_no=phonenumber,
                    full_name=fullname
                )
                user.save()
                messages.success(request, 'User registered successfully')
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    return render(request, 'register.html')

def login_register_view(request):
    return render(request, 'register.html')

