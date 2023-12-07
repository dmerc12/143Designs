from typing import List

from DAL.WorkDAL.WorkDALImplementation import WorkDALImplementation
from SAL.WorkSAL.WorkSALInterface import WorkSALInterface
from Entities.Work import Work


class WorkSALImplementation(WorkSALInterface):

    def __init__(self, work_dao: WorkDALImplementation):
        self.work_dao = work_dao

    def create_work(self, work: Work) -> Work:
        pass

    def get_work(self, work_id: int) -> Work:
        pass

    def get_all_work(self) -> List[Work]:
        pass

    def update_work(self, work: Work) -> bool:
        pass

    def delete_work(self, work_id: int) -> bool:
        pass
