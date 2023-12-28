from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ChangePasswordForm(PasswordChangeForm):
    pass
