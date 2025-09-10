from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages 
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required  
from django.contrib.auth import logout as auth_logout  
from django.views.decorators.cache import never_cache

from loans.models import LoanType



User = get_user_model()


# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/login/')
@never_cache
def user_dashboard(request):
    loan_types = LoanType.objects.all()  # fetch from DB
    return render(request, 'user_dashboard.html', {
        'user': request.user,
        'loan_types': loan_types
    })


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


def login_view(request):
    if request.user.is_authenticated:
        return redirect('user_dashboard')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('user_dashboard')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'login.html')


@login_required(login_url='/login/')
def logout_view(request):
    auth_logout(request)
    messages.info(request, "Logged out successfully")
    return redirect('login')



@login_required(login_url='/login/')
@never_cache
def profile(request):
    return render(request, 'profile.html', {'user': request.user})
  
    


 