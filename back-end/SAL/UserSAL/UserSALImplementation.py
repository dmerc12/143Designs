import logging

import bcrypt

from DAL.UserDAL.UserDALImplementation import UserDALImplementation
from Entities.CustomError import CustomError
from Entities.User import User
from SAL.UserSAL.UserSALInterface import UserSALInterface


class UserSALImplementation(UserSALInterface):

    def __init__(self, user_dao: UserDALImplementation):
        self.user_dao = user_dao

    def create_user(self, user: User, password_confirmation: str) -> User:
        logging.info("Beginning SAL method create user with user: " + str(user.convert_to_dictionary_full()) +
                     " and password confirmation: " + str(password_confirmation))
        if type(user.password) is not str:
            logging.warning("Error in SAL method create user, password not a string")
            raise CustomError("The password field must be a string, please try again!")
        elif len(user.password) > 60:
            logging.warning("Error in SAL method create user, password too long")
            raise CustomError("The password field cannot exceed 60 characters, please try again!")
        elif user.password == "":
            logging.warning("Error in SAL method create user, password empty")
            raise CustomError("The password field cannot be left  empty, please try again!")
        elif type(password_confirmation) is not str:
            logging.warning("Error in SAL method create user, confirmation password not a string")
            raise CustomError("The confirmation password field must be a string, please try again!")
        elif len(password_confirmation) > 60:
            logging.warning("Error in SAL method create user, confirmation password too long")
            raise CustomError("The confirmation password field cannot exceed 60 characters, please try again!")
        elif password_confirmation == "":
            logging.warning("Error in SAL method create user, confirmation password empty")
            raise CustomError("The confirmation password field cannot be left empty, please try again!")
        elif type(user.email) is not str:
            logging.warning("Error in SAL method create user, email not a string")
            raise CustomError("The email field must be a string, please try again!")
        elif len(user.email) > 60:
            logging.warning("Error in SAL method create user, email too long")
            raise CustomError("The email field cannot exceed 60 characters, please try again!")
        elif user.email == "":
            logging.warning("Error in SAL method create user, email empty")
            raise CustomError("The email field cannot be left empty, please try again!")
        elif user.password != password_confirmation:
            logging.warning("Error in SAL method create user, passwords don't match")
            raise CustomError("The passwords do not match, please try again!")
        else:
            result = self.get_user_by_email(user.email)
            if result.email == user.email:
                logging.warning("Error in SAL method create user, user already exists")
                raise CustomError("A user already exists with this email, please log in!")
            else:
                user.password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
                new_user = self.user_dao.create_user(user)
                logging.info("Finishing SAL method create user with user: " +
                             str(new_user.convert_to_dictionary_full()))
                return new_user

    def get_user_by_id(self, user_id: int) -> User:
        logging.info("Beginning SAL method get user by ID with user ID: " + str(user_id))
        if type(user_id) is not int:
            logging.warning("Error in SAL method get user by ID, user ID not integer")
            raise CustomError("User ID field must be an integer, please try again!")
        else:
            user = self.user_dao.get_user_by_id(user_id)
            if user.user_id == 0 and user.email == "" and user.password == "":
                logging.warning("Error in SAL method get user by ID, user not found")
                raise CustomError("This user cannot be found, please try again!")
            else:
                logging.info("Finishing SAL method get user by ID with user: " + str(user.convert_to_dictionary()))
                return user

    def get_user_by_email(self, email: str) -> User:
        logging.info("Beginning SAL method get user by email with email: " + str(email))
        if type(email) is not str:
            logging.warning("Error in SAL method get user by email, email not a string")
            raise CustomError("Email field must be a string, please try again!")
        else:
            user = self.user_dao.get_user_by_email(email)
            logging.info("Finishing SAL method get user by email with user: " + str(user.convert_to_dictionary()))
            return user

    def login(self, email: str, password: str) -> User:
        logging.info("Beginning SAL method login with email: " + str(email) + " and password: " + str(password))
        if type(email) is not str:
            logging.warning("Error in SAL method login, email not a string")
            raise CustomError("The email field must be a string, please try again!")
        elif email == "":
            logging.warning("Error in SAL method login, email empty")
            raise CustomError("The email field cannot be left empty, please try again!")
        elif type(password) is not str:
            logging.warning("Error in SAL method login, password not a string")
            raise CustomError("The password field must be a string, please try again!")
        elif password == "":
            logging.warning("Error in SAL method login, password empty")
            raise CustomError("The password field cannot be left empty, please try again!")
        else:
            user = self.user_dao.get_user_by_email(email)
            if (user.user_id == 0 and user.email == "" and user.password == "") or \
                    not bcrypt.checkpw(password.encode(), user.password.encode()):
                logging.warning("Error in SAL method login, incorrect email or password")
                raise CustomError("Either the email or password are incorrect, please try again!")
            else:
                logging.info("Finishing SAL method login with user: " + str(user.convert_to_dictionary()))
                return user

    def update_email(self, user: User) -> bool:
        logging.info("Beginning SAL method update user with user: " + str(user.convert_to_dictionary()))
        if type(user.user_id) is not int:
            logging.warning("Error in SAL method update user, user ID not an integer")
            raise CustomError("The user ID field must be an integer, please try again!")
        if type(user.email) is not str:
            logging.warning("Error in SAL method update user, email not a string")
            raise CustomError("The email field must be a string, please try again!")
        elif len(user.email) > 60:
            logging.warning("Error in SAL method update user, email too long")
            raise CustomError("The email field cannot exceed 60 characters, please try again!")
        elif user.email == "":
            logging.warning("Error in SAL method update user, email empty")
            raise CustomError("The email field cannot be empty, please try again!")
        else:
            current_info = self.get_user_by_id(user.user_id)
            if user.email == current_info.email:
                logging.warning("Error in SAL method update user, nothing changed")
                raise CustomError("No information has changed!")
            else:
                result = self.user_dao.update_email(user)
                logging.info("Finishing SAL method update user with user: " + str(result))
                return result

    def change_password(self, user: User, confirmation_password: str) -> bool:
        logging.info("Finishing SAL method change password with user: " + str(user.convert_to_dictionary()) +
                     " and confirmation password: " + str(confirmation_password))
        if type(user.password) is not str:
            logging.warning("Error in SAL method change password, new password not a string")
            raise CustomError("The password field must be a string, please try again!")
        elif len(user.password) > 60:
            logging.warning("Error in SAL method change password, new password too long")
            raise CustomError("The password field cannot exceed 60 characters, please try again!")
        elif user.password == "":
            logging.warning("Error in SAL method change password, new password empty")
            raise CustomError("The password field cannot be left empty, please try again!")
        elif type(confirmation_password) is not str:
            logging.warning("Error in SAL method change password, confirmation password not a string")
            raise CustomError("The confirmation password field must be a string, please try again!")
        elif len(confirmation_password) > 60:
            logging.warning("Error in SAL method change password, confirmation password too long")
            raise CustomError("The confirmation password field cannot exceed 60 characters, please try again!")
        elif confirmation_password == "":
            logging.warning("Error in SAL method change password, confirmation password empty")
            raise CustomError("The confirmation password cannot be left empty, please try again!")
        elif type(user.user_id) is not int:
            logging.warning("Error in SAL method change password user ID not an integer")
            raise CustomError("The user ID field must be an integer, please try again!")
        elif user.password != confirmation_password:
            logging.warning("Error in SAL method change password, passwords don't match")
            raise CustomError("The passwords don't match, please try again!")
        else:
            current_info = self.get_user_by_id(user.user_id)
            current_password = current_info.password.encode()
            if bcrypt.checkpw(user.password.encode("utf-8"), current_password):
                logging.warning("Error in SAL method change password, nothing changed")
                raise CustomError("Nothing has changed, please try again!")
            else:
                new_password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
                user.password = str(new_password)
                result = self.user_dao.change_password(user)
                logging.info("Finishing SAL method change password")
                return result

    def delete_user(self, user_id: int) -> bool:
        logging.info("Beginning SAL method delete user with user ID: " + str(user_id))
        if type(user_id) is not int:
            logging.warning("Error in SAL method delete user, user ID not an integer")
            raise CustomError("The user ID field must be an integer, please try again!")
        else:
            self.get_user_by_id(user_id)
            users = self.user_dao.get_all_users()
            if len(users) == 1:
                logging.warning("Error in SAL method delete user, last user")
                raise CustomError("Please create a new user, then try again!")
            else:
                result = self.user_dao.delete_user(user_id)
                logging.info("Finishing SAL method delete user")
                return result
