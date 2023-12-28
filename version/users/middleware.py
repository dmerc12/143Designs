from django.contrib.auth.models import User
from django.contrib import messages
class UserMiddleware:

    @staticmethod
    def create_user(request, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        confirmation_password = form.cleaned_data.get('confirmation_password')
        form.save()
        messages.success(request, f'Account created for {username}!')

    @staticmethod
    def update_user(request, form):
        form.save()
        messages.success(request, 'Your account has been updated!')

    @staticmethod
    def change_password(request, form):
        form.save()
        messages.success(request, 'Your password has been changed!')

    @staticmethod
    def delete_user(request):
        request.user.delete()
        messages.success(request, 'Your account has been deleted, goodbye!')
        