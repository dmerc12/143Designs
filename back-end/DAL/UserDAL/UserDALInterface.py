from abc import ABC, abstractmethod

from Entities.User import User


class UserDALInterface(ABC):

    @abstractmethod
    def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    def login(self, email: str, password: str) -> User:
        pass

    @abstractmethod
    def update_user(self, user: User) -> User:
        pass

    @abstractmethod
    def change_password(self, user_id: int, password: str) -> bool:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        pass
