from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirmation_password']

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ChangePasswordForm(PasswordChangeForm):
    pass
