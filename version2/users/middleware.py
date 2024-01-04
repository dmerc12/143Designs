import logging
from django.contrib import messages
from django.contrib.auth.models import User

class UserMiddleware:

    @staticmethod
    def create_user(request, form):
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        logging.info('Beginning user middleware method create user with username: ' + str(username) + ', email: ' + str(email))
        form.save()
        logging.info('Finishing user middleware method create user')
        messages.success(request, f'Account created for {username}!')

    @staticmethod
    def update_user(request, form):
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        logging.info('Beginning user middleware method update user with username: ' + str(username) + ', email: ' + str(email))
        current_info = request.user
        if current_info.username == username and current_info.email == email:
            logging.warning('Error in user middleware method update user, nothing changed!')
            raise RuntimeError('Nothing changed!, please try again!')
        else:
            form.save()
            logging.info('Finishing user middleware method update user')
            messages.success(request, 'Your account has been updated!')

    @staticmethod
    def change_password(request, form):
        logging.info('Beginning user middleware method change password')
        form.save()
        logging.info('Finishing user middleware method change password')
        messages.success(request, 'Your password has been changed!')

    @staticmethod
    def delete_user(request):
        logging.info('Beginning user middleware method delete user')
        if User.objects.exclude(pk=request.user.pk).exists():
            request.user.delete()
            logging.info('Finishing user middleware method delete user')
            messages.success(request, 'Your account has been deleted, goodbye!')
        else:
            logging.warning('Error in user middleware method delete user, current user is the last user in the database')
            raise RuntimeError('Another user must be created before your profile can be deleted')
