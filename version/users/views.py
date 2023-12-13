from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm

from .forms import UserRegisterForm, UserUpdateForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'users/home.html')

@login_required
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form':  form})

@login_required
def update_user(request):
    if request.method == 'POST':
        update_form = UserUpdateForm(request.POST, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect('home')
        else:
            update_form = UserUpdateForm(instance=request.user)
            return render(request, 'users/update.html', {'update_form': update_form})
    else:
        update_form = UserUpdateForm(instance=request.user)
        return render(request, 'users/update.html', {'update_form': update_form})

@login_required
def change_password(request):
    if request.method == 'POST':
        change_password_form = PasswordChangeForm(user=request.user)
        if change_password_form.is_valid():
            change_password_form.save()
            messages.success(request, "Your password has been changed!")
            return redirect('home')
        else:
            change_password_form = PasswordChangeForm(user=request.user)
            return render(request, 'users/change_password.html', {'change_password': change_password_form})
    else:
        change_password_form = PasswordChangeForm(user=request.user)
        return render(request, 'users/change_password.html', {'change_password': change_password_form})
