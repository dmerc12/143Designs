from .forms import LoginForm, RegisterForm, UpdateUserForm, ChangePasswordForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser

# View for home page
def home(request):
    return render(request, 'home.html')

# View for admin home page
def admin_home(request):
    return render(request, 'admin_home.html')

# View for login page
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            base_user = authenticate(request, username=username, password=password)
            if base_user is not None:
                login(request, base_user)
                user = CustomUser.objects.get(user=base_user)
                messages.success(request, f'Welcome {base_user.first_name} {base_user.last_name}!')
                if user.role == 'admin':
                    return redirect('admin-home')
                else:
                    return redirect('home')
            else:
                messages.error(request, 'Incorrect username or password, please try again!')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

# View for logout functionality
def logout_user(request):
    logout(request)
    messages.success(request, 'Goodbye!')
    return redirect('home')

# View for register page
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            user = form.save()
            CustomUser.objects.create(user=user, phone_number=phone_number, role='user')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Your account has been created and you have been logged in!\nWelcome {user.first_name} {user.last_name}!')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

# View for update user page

# View for change password page

# View for delete user page
