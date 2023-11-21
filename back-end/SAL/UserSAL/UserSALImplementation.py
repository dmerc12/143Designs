import logging

from DAL.UserDAL.UserDALImplementation import UserDALImplementation
from SAL.UserSAL.UserSALInterface import UserSALInterface
from Entities.CustomError import CustomError
from Entities.User import User


class UserSALImplementation(UserSALInterface):

    def __init__(self, user_dao: UserDALImplementation):
        self.user_dao = user_dao

    def create_user(self, user: User, confirmation_password: str) -> User:
        pass

    def get_user_by_id(self, user_id: int) -> User:
        pass

    def get_user_by_email(self, email: str) -> User:
        pass

    def login(self, email: str, password: str) -> User:
        pass

    def update_email(self, user: User) -> User:
        pass

    def change_password(self, user: User, confirmation_password: str) -> bool:
        pass

    def delete_user(self, user_id: int) -> bool:
        pass
