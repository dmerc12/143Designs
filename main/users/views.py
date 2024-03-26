from .forms import LoginForm, RegisterForm, UpdateUserForm, ChangePasswordForm, AdminChangePasswordForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import CustomUser

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
                messages.success(request, f'Welcome {base_user.first_name} {base_user.last_name}!')
                if  (request.user.is_superuser and request.user.is_activ) or (CustomUser.objects.get(user=base_user).role == 'admin' and CustomUser.objects.get(user=base_user).active):
                    return redirect('admin')
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
    return render(request, 'users/users/register.html', {'form': form})

# View for update user page
def update_user(request):
    if request.user.is_authenticated:
        base_user = User.objects.get(pk=request.user.pk)
        user = CustomUser.objects.get(user=base_user.pk)
        if request.method == 'POST':
            form = UpdateUserForm(request.POST, instance=base_user)
            if form.is_valid():
                form.save()
                user.phone_number = form.cleaned_data['phone_number']
                user.save()
                login(request, base_user)
                messages.success(request, 'Your account has been successfully updated!')
                return redirect('home')
        else:
            form = UpdateUserForm(instance=base_user)
            form.initial['phone_number'] = user.phone_number
        return render(request, 'users/users/update.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to access this page. Please register or login then try again!')
        return redirect('login')

# View for change password page
def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangePasswordForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                login(request, request.user)
                messages.success(request, 'Your password has been successfully changed!')
                return redirect('home')
        else:
            form = ChangePasswordForm(request.user)
        return render(request, 'users/users/change_password.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to access this page. Please register or login then try again!')
        return redirect('login')

# View for delete user page
def delete_user(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            request.user.delete()
            logout(request)
            messages.success(request, 'Your profile has been successfully deleted, goodbye!')
            return redirect('home')
        return render(request, 'users/users/delete.html')
    else:
        messages.error(request, 'You must be logged in to access this page. Please register or login then try again!')
        return redirect('login')

# View for admin home page
def admin_home(request):
    if (request.user.is_superuser or CustomUser.objects.filter(user=request.user.id, role='admin').exists()) and request.user.is_authenticated:
        superusers = User.objects.filter(is_superuser=True)
        admins = CustomUser.objects.filter(role='admin')
        all_admins = list(superusers) + list(admins)
        return render(request, 'users/admin/home.html', {'admins': all_admins})
    else:
        messages.error(request, 'You must be a site admin access this page!')
        return redirect('home')

# View for register admin page
def register_admin(request):
    if (request.user.is_superuser or CustomUser.objects.filter(user=request.user.id, role='admin').exists()) and request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                phone_number = form.cleaned_data['phone_number']
                user = form.save()
                CustomUser.objects.create(user=user, phone_number=phone_number, role='admin')
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, f'Admin account {user.first_name} {user.last_name} has been created and they can now use their credentials to login!')
                return redirect('admin-home')
        else:
            form = RegisterForm()
        return render(request, 'users/admin/register.html', {'form': form})
    else:
        messages.error(request, 'You must be a site admin access this page!')
        return redirect('home')

# View for activate admin page
def activate_admin(request, admin_id):
    if (request.user.is_superuser or CustomUser.objects.filter(user=request.user.id, role='admin').exists()) and request.user.is_authenticated:
        admin = CustomUser.objects.get(pk=admin_id)
        if request.method == 'POST':
            admin.active = True
            admin.save()
            messages.success(request, f'The profile for {admin.user.first_name} {admin.user.last_name} has been activated!')
            return redirect('admin-home')
        return render(request, 'users/admin/activate.html', {'admin': admin})
    else:
        messages.error(request, 'You must be a site admin access this page!')
        return redirect('home')

# View for deactivate admin page
def deactivate_admin(request, admin_id):
    if (request.user.is_superuser or CustomUser.objects.filter(user=request.user.id, role='admin').exists()) and request.user.is_authenticated:
        admin = CustomUser.objects.get(pk=admin_id)
        if request.method == 'POST':
            admin.active = False
            admin.save()
            messages.warning(request, f'The profile for {admin.user.first_name} {admin.user.last_name} has been deactivated!')
            return redirect('admin-home')
        return render(request, 'users/admin/deactivate.html', {'admin': admin})
    else:
        messages.error(request, 'You must be a site admin access this page!')
        return redirect('home')

# View for admin reset password page
def admin_reset_password(request, user_id):
    if (request.user.is_superuser or CustomUser.objects.filter(user=request.user.id, role='admin').exists()) and request.user.is_authenticated:
        user = User.objects.get(pk=user_id)
        if request.method == 'POST':
            form = AdminChangePasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                login(request, request.user)
                messages.success(request, f'The password for {user.first_name} {user.last_name} has been reset!')
                return redirect('admin-home')
        else:
            form = AdminChangePasswordForm(user)
        return render(request, 'users/admin/reset_password.html', {'form': form, 'user': user})
    else:
        messages.error(request, 'You must be a site admin access this page!')
        return redirect('home')
