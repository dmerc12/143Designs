import logging
from typing import List

from DAL.WorkDAL.WorkDALImplementation import WorkDALImplementation
from Entities.CustomError import CustomError
from SAL.WorkSAL.WorkSALInterface import WorkSALInterface
from Entities.Work import Work


class WorkSALImplementation(WorkSALInterface):

    def __init__(self, work_dao: WorkDALImplementation):
        self.work_dao = work_dao

    def create_work(self, work: Work) -> Work:
        logging.info("Beginning SAL method create work with work: " + str(work.convert_to_dictionary()))
        if type(work.name) is not str:
            logging.warning("Error in SAL method create work, name not a string")
            raise CustomError("The name field must be a string, please try again!")
        elif len(work.name) > 60:
            logging.warning("Error in SAL method create work, name too long")
            raise CustomError("The name field cannot exceed 60 characters, please try again!")
        elif type(work.description) is not str:
            logging.warning("Error in SAL method create work, description not a string")
            raise CustomError("The description field must be a string, please try again!")
        elif len(work.description) > 255:
            logging.warning("Error in SAL method create work, description too long")
            raise CustomError("The description field cannot exceed 255 characters, please try again!")
        elif work.description == "":
            logging.warning("Error in SAL method create work, description empty")
            raise CustomError("The description field cannot be left empty, please try again!")
        else:
            work = self.work_dao.create_work(work)
            logging.info("Finishing SAL method create work with work: " + str(work.convert_to_dictionary()))
            return work

    def get_work(self, work_id: int) -> Work:
        logging.info("Beginning SAL method get work with work ID: " + str(work_id))
        if type(work_id) is not int:
            logging.warning("Error in SAL method get work, work ID not an integer")
            raise CustomError("The work ID field must be an integer, please try again!")
        else:
            work = self.work_dao.get_work(work_id)
            if work.work_id == 0 and work.name == "" and work.description == "":
                logging.warning("Error in SAL method get work, work not found")
                raise CustomError("Work not found, please try again!")
            else:
                logging.info("Finishing SAL method get work with work: " + str(work.convert_to_dictionary()))
                return work

    def get_all_work(self) -> List[Work]:
        logging.info("Beginning SAL method get all work")
        works = self.work_dao.get_all_work()
        if len(works) == 0:
            logging.warning("Error in SAL method get all work, none found")
            raise CustomError("No works found, please try again!")
        else:
            logging.info("Finishing SAL method get all work")
            return works

    def update_work(self, work: Work) -> bool:
        logging.info("Beginning DAL method update work with work: " + str(work.convert_to_dictionary()))
        if type(work.work_id) is not int:
            logging.warning("Error in SAL method update work, work ID not an integer")
            raise CustomError("The work ID field must be an integer, please try again!")
        elif type(work.name) is not str:
            logging.warning("Error in SAL method update work, name not a string")
            raise CustomError("The name field must be a string, please try again!")
        elif len(work.name) > 60:
            logging.warning("Error in SAL method update work, name too long")
            raise CustomError("The name field cannot exceed 60 characters please try again!")
        elif type(work.description) is not str:
            logging.warning("Error in SAL method update work, description not a string")
            raise CustomError("The description field must be a string, please try again!")
        elif len(work.description) > 255:
            logging.warning("Error in SAL method update work, description too long")
            raise CustomError("The description field cannot exceed 255 characters, please try again!")
        elif work.description == "":
            logging.warning("Error in SAL method update work, description left empty")
            raise CustomError("The description field cannot be left empty, please try again!")
        else:
            self.get_work(work.work_id)
            result = self.work_dao.update_work(work)
            logging.info("Finishing SAL method update work")
            return result

    def delete_work(self, work_id: int) -> bool:
        logging.info("Beginning SAL method delete work with work ID: " + str(work_id))
        if type(work_id) is not int:
            logging.warning("Error in SAL method delete work, work ID not an integer")
            raise CustomError("The work ID field must be an integer, please try again!")
        else:
            self.get_work(work_id)
            result = self.work_dao.delete_work(work_id)
            logging.info("Finishing SAL method delete work")
            return result
