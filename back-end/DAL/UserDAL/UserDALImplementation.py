import logging

from DAL.UserDAL.UserDALInterface import UserDALInterface
from Database.DBConnection import DBConnection
from Entities.User import User


class UserDALImplementation(UserDALInterface):

    def create_user(self, user: User) -> User:
        pass

    def get_user_by_id(self, user_id: int) -> User:
        pass

    def get_user_by_email(self, email: str) -> User:
        pass

    def login(self, email: str, password: str) -> User:
        pass

    def update_user(self, user: User) -> User:
        pass

    def change_password(self, user_id: int, password: str) -> bool:
        pass

    def delete_user(self, user_id: int) -> bool:
        pass
