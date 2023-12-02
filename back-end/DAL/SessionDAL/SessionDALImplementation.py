import logging
from datetime import datetime

from DAL.SessionDAL.SessionDALInterface import SessionDALInterface
from Database.DBConnection import DBConnection
from Entities.Session import Session

class SessionDALImplementation(SessionDALInterface):

    def create_session(self, session: Session) -> Session:
        logging.info("Beginning DAL method create session with session: " + str(session.convert_to_dictionary()))
        sql = "INSERT INTO Designs.Session (session_id, user_id, expiration) VALUES (%s, %s, %s);"
        connection = DBConnection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (session.session_id, session.user_id, session.expiration))
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method create session with session: " + str(session.convert_to_dictionary()))
        return session

    def get_session(self, session_id: str) -> Session:
        logging.info("Beginning DAL method get session with session ID: " + str(session_id))
        sql = "SELECT * FROM Designs.Session WHERE session_id=%s;"
        connection = DBConnection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (session_id,))
        session_info = cursor.fetchone()
        cursor.close()
        connection.close()
        if session_info is None:
            session = Session("0", 0, datetime(1, 1, 1))
            logging.warning("Finishing DAL method get session, not found")
            return session
        else:
            session = Session(*session_info)
            logging.info("Finishing DAL method get session with session: " + str(session.convert_to_dictionary()))
            return session

    def update_session(self, session: Session) -> bool:
        logging.info("Beginning DAL method update session with session: " + str(session.convert_to_dictionary()))
        sql = "UPDATE Designs.Session SET expiration=%s WHERE session_id=%s;"
        connection = DBConnection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (session.expiration, session.session_id))
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method update session")
        return True

    def delete_session(self, session_id: str) -> bool:
        logging.info("Beginning DAL method delete session with session ID: " + str(session_id))
        sql = "DELETE FROM Designs.Session WHERE session_id=%s;"
        connection = DBConnection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (session_id,))
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method delete session")
        return True

    def delete_all_sessions(self, user_id: int) -> bool:
        logging.info("Beginning DAL method delete all sessions with user ID: " + str(user_id))
        sql = "DELETE FROM Designs.Session WHERE user_id=%s;"
        connection = DBConnection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (user_id,))
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method delete all sessions")
        return True
