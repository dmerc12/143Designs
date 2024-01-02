import logging
from typing import List

from DAL.WorkDAL.WorkDALInterface import WorkDALInterface
from Database.DBConnection import DBConnection
from Entities.Work import Work


class WorkDALImplementation(WorkDALInterface):

    def create_work(self, work: Work) -> Work:
        logging.info("Beginning DAL method create work with work: " + str(work.convert_to_dictionary()))
        sql = "INSERT INTO Designs.Work (name, description) VALUES (%s, %s) RETURNING work_id;"
        connection = DBConnection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (work.name, work.description))
        work.work_id = cursor.fetchone()[0]
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method create work with work: " + str(work.convert_to_dictionary()))
        return work

    def get_work(self, work_id: int) -> Work:
        logging.info("Beginning DAL method get work with work ID: " + str(work_id))
        sql = "SELECT * FROM Designs.Work WHERE work_id=%s;"
        connection = DBConnection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (work_id,))
        work_info = cursor.fetchone()
        cursor.close()
        if work_info is None:
            work = Work(0, "", "")
            logging.warning("Finishing DAL method get work, work not found")
            return work
        else:
            work = Work(*work_info)
            logging.info("Finishing DAL method get work with work: " + str(work.convert_to_dictionary()))
            return work

    def get_all_work(self) -> List[Work]:
        logging.info("Beginning DAL method get all work")
        sql = "SELECT * FROM Designs.Work;"
        connection = DBConnection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql)
        work_records = cursor.fetchall()
        cursor.close()
        connection.close()
        work_list = []
        for work in work_records:
            work = Work(*work)
            work_list.append(work)
            logging.info("Finishing DAL method get all work with work: " + str(work.convert_to_dictionary()))
        return work_list

    def update_work(self, work: Work) -> bool:
        logging.info("Beginning DAL method update work with work: " + str(work.convert_to_dictionary()))
        sql = "UPDATE Designs.Work SET name=%s, description=%s WHERE work_id=%s;"
        connection = DBConnection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (work.name, work.description, work.work_id))
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method update work")
        return True

    def delete_work(self, work_id: int) -> bool:
        logging.info("Beginning DAL method delete work with work ID: " + str(work_id))
        sql = "DELETE FROM Designs.Work WHERE work_id=%s;"
        connection = DBConnection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (work_id,))
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method delete work")
        return True
