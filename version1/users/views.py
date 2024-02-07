from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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

# Logout view for customer site of website
def logout_customer(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out!')
    return redirect('home')
