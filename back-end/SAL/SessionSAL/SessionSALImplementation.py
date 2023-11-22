import logging
from datetime import date, datetime

from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from DAL.UserDAL.UserDALImplementation import UserDALImplementation
from SAL.UserSAL.UserSALImplementation import UserSALImplementation
from SAL.SessionSAL.SessionSALInterface import SessionSALInterface
from Entities.CustomError import CustomError
from Entities.Session import Session


class SessionSALImplementation(SessionSALInterface):
    user_dao = UserDALImplementation()
    user_sao = UserSALImplementation(user_dao)

    def __init__(self, session_dao: SessionDALImplementation):
        self.session_dao = session_dao

    def create_session(self, session: Session) -> Session:
        pass

    def get_session(self, session_id: int) -> Session:
        pass

    def update_session(self, session: Session) -> bool:
        pass

    def delete_session(self, session_id: int) -> bool:
        pass

    def delete_all_sessions(self, user_id: int) -> bool:
        pass
