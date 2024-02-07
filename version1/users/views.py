from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Login view for customer side of website
def login_customer(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        customer = authenticate(request, username=username, password=password)
        if customer is not None:
            login(request, customer)
            messages.success(request, 'You have been successfully logged in!')
            return redirect('store-home')
        else:
            messages.error(request, 'Incorrect username or password, please try again!')
            return redirect('login')
    else:
        return render(request, 'users/login.html')

# Logout view for customer side of website
def logout_customer(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out!')
    return redirect('home')

# Register view for customer side of website
def register_customer(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You Have Registered Successfully! Welcome!')
            return redirect('home')
        else:
            messages.success(request, 'Whoops! There was an error processing your registration, please try again!')
            return redirect('register')
    else:
        form = SignUpForm()
        return render(request, 'users/register.html', {'form': form})
