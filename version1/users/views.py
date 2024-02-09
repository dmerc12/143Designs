from .forms import LoginForm, SignUpForm, UpdateCustomerForm, ChangePasswordForm, UpdateInfoForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Customer

# Login view for customer side of website
def login_customer(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            customer = authenticate(request, username=username, password=password)
            if customer is not None:
                login(request, customer)
                messages.success(request, f'Welcome {customer.first_name}!')
                return redirect('store-home')
            else:
                messages.error(request, 'Incorrect username or password, please try again!')
                return redirect('login')
        else:
            messages.error(request, 'Incorrect username or password, please try again!')
            return redirect('login')
    else:
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

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
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have registered successfully! Please add your address below!')
            return redirect('update-address')
        else:
            messages.success(request, 'Whoops! There was an error processing your registration, please try again!')
            return redirect('register')
    else:
        form = SignUpForm()
        return render(request, 'users/register.html', {'form': form})

# Update customer profile view for customer side of website
def update_customer(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        form = UpdateCustomerForm(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            login(request, current_user)
            messages.success(request, 'Your profile has been successfully updated!')
            return redirect('update-customer')
        else:
            return render(request, 'users/update_customer.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to access this page. Please log in then try again!')
        return redirect('login')

# Change password view for customer side of website
def change_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                login(request, current_user)
                messages.success(request, 'Your password has been changed!')
                return redirect('update-customer')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                return redirect('change-password')
        else:
            form = ChangePasswordForm(current_user)
            return render(request, 'users/update_password.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to access this page. Please log in then try again!')
        return redirect('login')

# Update customer info view for customer side of website
def update_address(request):
    if request.user.is_authenticated:
        current_user = Customer.objects.get(id=request.user.id)
        form = UpdateInfoForm(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your address has been successfully updated!')
            return redirect('update-customer')
        else:
            return render(request, 'users/update_address.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to access this page. Please log in then try again!')
        return redirect('login')
