import logging
from django.contrib import messages

class UserMiddleware:

    @staticmethod
    def create_user(request, form):
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        confirmation_password = form.cleaned_data.get('confirmation_password')
        logging.info('Beginning user middleware method create user with username: ' + str(username) + ', email: ' + str(email))
        if type(username) is not str:
            logging.warning('Error in user middleware method create user, username not a string')
            raise RuntimeError('The username field must be a string, please try again!')
        elif len(username) > 60:
            logging.warning('Error in user middleware create user, username too long')
            raise RuntimeError('The username field cannot exceed 60 characters, please try again!')
        elif username == '':
            logging.warning('Error in user middleware method create user, username left empty')
            raise RuntimeError('The username field cannot be left empty, please try again!')
        elif type(email) is not str:
            logging.warning('Error in user middleware method create user, email not a string')
            raise RuntimeError('The email field must be a string, please try again!')
        elif len(email) > 60:
            logging.warning('Error in user middleware method create user, email too long')
            raise RuntimeError('The email field cannot exceed 60 characters, please try again!')
        elif email == '':
            logging.warnig('Error in user middleware method create user email left empty')
            raise RuntimeError('The email field cannot be left empty, please try again!')
        elif type(password) is not str:
            logging.warning('Error in user middleware method create user, password not a string')
            raise RuntimeError('The password field must be a string, please try again!')
        elif len(password) > 60:
            logging.warning('Error in user middleware method create user, password too long')
            raise RuntimeError('The password field cannot exceed 60 characters, please try again!')
        elif password == '':
            logging.warning('Error in user middleware method create user, password left empty')
            raise RuntimeError('The password field cannot be left empty, please try again!')
        elif type(confirmation_password) is not str:
            logging.warning('Error in user middleware method create user, confirmation password not a string')
            raise RuntimeError('The confirmation password must be a string, please try again!')
        elif len(confirmation_password) > 60:
            logging.warning('Error in user middleware method create user, confirmation password too long')
            raise RuntimeError('The confirmation password cannot exceed 60 characters, please try again!')
        elif confirmation_password == '':
            logging.warning('Error in user middleware method create user, confirmation password left empty')
            raise RuntimeError('The confirmation password cannot be left empty, please try again!')
        else:
            logging.info('Finishing user middleware method create user')
            form.save()
            messages.success(request, f'Account created for {username}!')

    @staticmethod
    def update_user(request, form):
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        logging.info('Beginning user middleware method update user with username: ' + str(username) + ', email: ' + str(email))
        if type(username) is not str:
            logging.warning('Error in user middleware method update user, username not a string')
            raise RuntimeError('The username field must be a string, please try again!')
        elif len(username) > 60:
            logging.warning('Error in user middleware update user, username too long')
            raise RuntimeError('The username field cannot exceed 60 characters, please try again!')
        elif username == '':
            logging.warning('Error in user middleware method update user, username left empty')
            raise RuntimeError('The username field cannot be left empty, please try again!')
        elif type(email) is not str:
            logging.warning('Error in user middleware method update user, email not a string')
            raise RuntimeError('The email field must be a string, please try again!')
        elif len(email) > 60:
            logging.warning('Error in user middleware method update user, email too long')
            raise RuntimeError('The email field cannot exceed 60 characters, please try again!')
        elif email == '':
            logging.warnig('Error in user middleware method update user email left empty')
            raise RuntimeError('The email field cannot be left empty, please try again!')
        else:
            current_info = request.user
            if current_info.username == username and current_info.email == email:
                logging.warning('Error in user middleware method update user, nothing changed!')
                raise RuntimeError('Nothing changed!, please try again!')
            else:
                logging.info('Finishing user middleware method update user')
                form.save()
                messages.success(request, 'Your account has been updated!')

    @staticmethod
    def change_password(request, form):
        password = form.cleaned_data.get('password')
        confirmation_password = form.cleaned_data.get('confirmation_password')
        logging.info('Beginning user middleware method change password')
        if type(password) is not str:
            logging.warning('Error in user middleware method change password, password not a string')
            raise RuntimeError('The password field must be a string, please try again!')
        elif len(password) > 60:
            logging.warning('Error in user middleware method change password, password too long')
            raise RuntimeError('The password field cannot exceed 60 characters, please try again!')
        elif password == '':
            logging.warning('Error in user middleware method change password, password empty')
            raise RuntimeError('The password field cannot be left empty, please try again!')
        elif type(confirmation_password) is not str:
            logging.warning('Error in user middleware method change password, confirmation password not a string')
            raise RuntimeError('The confirmation password field must be a string, please try again!')
        elif len(confirmation_password) > 60:
            logging.warning('Error in user middleware method change password, confirmation password too long')
            raise RuntimeError('The confirmation password field cannot exceed 60 characters, please try again!')
        elif confirmation_password == '':
            logging.warning('Error in user middleware method change password, confirmation password empty')
            raise RuntimeError('The confirmation password field cannot be left empty, please try again!')
        else:
            logging.info('Finishing user middleware method change password')
            form.save()
            messages.success(request, 'Your password has been changed!')

    @staticmethod
    def delete_user(request):
        request.user.delete()
        messages.success(request, 'Your account has been deleted, goodbye!')
