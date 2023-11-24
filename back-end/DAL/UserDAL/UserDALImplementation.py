import logging
from typing import List

from DAL.UserDAL.UserDALInterface import UserDALInterface
from Database.DBConnection import DBConnection
from Entities.User import User


class UserDALImplementation(UserDALInterface):

    def create_user(self, user: User) -> User:
        logging.info("Beginning DAL method create user with user: " + str(user.convert_to_dictionary_full()))
        sql = "INSERT INTO 143Designs.User (email, passwrd) VALUES (%s, %s);"
        connection = DBConnection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (user.email, user.password))
        connection.commit()
        user_id = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        user.user_id = user_id
        logging.info("Finishing DAL method create user")
        return user

    def get_user_by_id(self, user_id: int) -> User:
        logging.info("Beginning DAL method get user by ID with ID: " + str(user_id))
        sql = "SELECT * FROM 143Designs.User WHERE user_id=%s;"
        connection = DBConnection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (user_id,))
        user_info = cursor.fetchone()
        cursor.close()
        connection.close()
        if user_info is None:
            user = User(0, "", "")
            logging.warning("Finishing DAL method get user by ID, user not found")
            return user
        else:
            user = User(*user_info)
            logging.info("Finishing DAL method get user by ID with user: " + user.convert_to_dictionary())
            return user

    def get_user_by_email(self, email: str) -> User:
        logging.info("Beginning DAL method get user by email with email: " + email)
        sql = "SELECT * FROM 143Designs.User WHERE email=%s;"
        connection = DBConnection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (email,))
        user_info = cursor.fetchone()
        cursor.close()
        connection.close()
        if user_info is None:
            user = User(0, "", "")
            logging.warning("Finishing DAL method get user by email, user not found")
            return user
        else:
            user = User(*user_info)
            logging.info("Finishing DAL method get user by email with user: " + user.convert_to_dictionary())
            return user

    def get_all_users(self) -> List[User]:
        pass

    def login(self, email: str, password: str) -> User:
        logging.info("Beginning DAL method login with email: " + email + " and password: " + password)
        sql = "SELECT * FROM 143Designs.User WHERE email=%s and passwrd=%s;"
        connection = DBConnection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (email, password))
        user_info = cursor.fetchone()
        cursor.close()
        connection.close()
        if user_info is None:
            user = User(0, "", "")
            logging.warning("Finishing DAL method login, user not found")
            return user
        else:
            user = User(*user_info)
            logging.info("Finishing DAL method login with user: " + str(user.convert_to_dictionary()))
            return user

    def update_email(self, user: User) -> User:
        logging.info("Beginning DAL method update email with user: " + str(user.convert_to_dictionary()))
        sql = "UPDATE 143Designs.User SET email=%s WHERE user_id=%s;"
        connection = DBConnection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (user.email, user.user_id))
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method update email with result: " + str(user.convert_to_dictionary()))
        return user

    def change_password(self, user: User) -> bool:
        logging.info("Beginning DAL method change password with user: ")
        sql = "UPDATE 143Designs.User SET passwrd=%s WHERE user_id=%s;"
        connection = DBConnection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (user.password, user.user_id))
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method change password")
        return True

    def delete_user(self, user_id: int) -> bool:
        logging.info("Beginning DAL method delete user with user ID: " + str(user_id))
        sql = "DELETE FROM 143Designs.User WHERE user_id=%s;"
        connection = DBConnection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (user_id,))
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method delete user")
        return True
