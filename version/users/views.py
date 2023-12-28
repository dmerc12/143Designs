from .forms import AddUserForm, UpdateUserForm, ChangePasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .middleware import UserMiddleware

middleware = UserMiddleware()

@login_required
def home(request):
    users = User.objects.all()
    return render(request, 'users/home.html', {'users': users})

@login_required
def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            middleware.create_user(request, form)
            return redirect('user-home')
    else:
        form = AddUserForm()
    return render(request, 'users/register.html', {'form':  form})

@login_required
def update_user(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            middleware.update_user(request, form)
            return redirect('user-home')
    else:
        form = UpdateUserForm(instance=request.user)
    return render(request, 'users/update.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            middleware.change_password(request, form)
            return redirect('user-home')
    else:
        form = ChangePasswordForm(user=request.user)
    return render(request, 'users/change_password.html', {'form': form})

@login_required
def delete_user(request):
    if request.method == 'POST':
        middleware.delete_user(request)
        return redirect('user-home')
    return render(request, 'users/delete.html')
