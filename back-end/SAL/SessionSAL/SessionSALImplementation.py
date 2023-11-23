import logging
from datetime import datetime

from DAL.SessionDAL.SessionDALImplementation import SessionDALImplementation
from DAL.UserDAL.UserDALImplementation import UserDALImplementation
from SAL.UserSAL.UserSALImplementation import UserSALImplementation
from SAL.SessionSAL.SessionSALInterface import SessionSALInterface
from Entities.CustomError import CustomError
from Database.IDGenerator import IDGenerator
from Entities.Session import Session


class SessionSALImplementation(SessionSALInterface):
    user_dao = UserDALImplementation()
    user_sao = UserSALImplementation(user_dao)
    id_generator = IDGenerator()

    def __init__(self, session_dao: SessionDALImplementation):
        self.session_dao = session_dao

    def create_session(self, session: Session) -> Session:
        logging.info("Beginning SAL method create session with session: " + str(session.convert_to_dictionary()))
        if type(session.user_id) is not int:
            logging.warning("Error in SAL method create session, user ID not an integer")
            raise CustomError("The user ID field must be an integer, please try again!")
        elif type(session.expiration) is not datetime:
            logging.warning("Error in SAL method create session, expiration not a datetime")
            raise CustomError("The expiration field must be a datetime, please try again!")
        elif session.expiration < datetime.now():
            logging.warning("Error in SAL method create session, expiration already the past")
            raise CustomError("The expiration field must be in the future, please try again!")
        else:
            self.user_sao.get_user_by_id(session.user_id)
            session.session_id = self.id_generator.generate_id()
            session = self.session_dao.create_session(session)
            session.session_id = session.session_id + self.id_generator.generate_salt()
            logging.info("Finishing SAL method create session with session: " + str(session.convert_to_dictionary()))
            return session

    def get_session(self, session_id: str) -> Session:
        logging.info("Beginning SAL method get session with session ID: " + str(session_id))
        if type(session_id) is not str:
            logging.warning("Error in SAL method get session, session ID not a strint")
            raise CustomError("The session ID field must be a string, please try again!")
        else:
            session_id = self.id_generator.remove_salt(session_id)
            session = self.session_dao.get_session(session_id)
            if session.session_id == "0" and session.user_id == 0 and \
                    session.expiration == datetime(0000, 00, 00, 00, 00, 00, 00):
                logging.warning("Error in SAL method get session, session not found")
                raise CustomError("No session found, please try again!")
            elif session.expiration < datetime.now():
                logging.warning("Error in SAL method get session, session expired")
                raise CustomError("Session has expired, please log in!")
            else:
                logging.info("Finishing SAL method get session with session: " + str(session.convert_to_dictionary()))
                return session

    def update_session(self, session: Session) -> bool:
        logging.info("Beginning SAL method update session with session with session: " +
                     str(session.convert_to_dictionary()))
        if type(session.session_id) is not str:
            logging.warning("Error in SAL method update session, session ID not a string")
            raise CustomError("The session ID field must be a string, please try again!")
        elif type(session.user_id) is not int:
            logging.warning("Error in SAL method update session, user ID not an integer")
            raise CustomError("The user ID field must be an integer, please try again!")
        elif type(session.expiration) is not datetime:
            logging.warning("Error in SAL method update session, expiration not a datetime")
            raise CustomError("The expiration field must be a datetime, please try again!")
        elif session.expiration < datetime.now():
            logging.warning("Error in SAL method update session, expiration already past")
            raise CustomError("The expiration field must be in the future, please try again!")
        else:
            self.get_session(session.session_id)
            result = self.session_dao.update_session(session)
            logging.info("Finishing SAL method update session with result: " + str(result))
            return result

    def delete_session(self, session_id: str) -> bool:
        logging.info("Beginning SAL method delete session with session ID: " + str(session_id))
        if type(session_id) is not str:
            logging.warning("Error in SAL method delete session, session ID not a string")
            raise CustomError("The session ID field must be a string, please try again!")
        else:
            self.get_session(session_id)
            result = self.session_dao.delete_session(session_id)
            logging.info("Finishing SAL method delete session with result: " + str(result))
            return result

    def delete_all_sessions(self, user_id: int) -> bool:
        logging.info("Beginning SAL method delete all sessions with user ID: " + str(user_id))
        if type(user_id) is not int:
            logging.warning("Error in SAL method delete all sessions, user ID not an integer")
            raise CustomError("The user ID field must be an integer, please try again!")
        else:
            self.user_sao.get_user_by_id(user_id)
            result = self.session_dao.delete_all_sessions(user_id)
            logging.info("Finishing SAL method delete all sessions with result: " + str(result))
            return result
