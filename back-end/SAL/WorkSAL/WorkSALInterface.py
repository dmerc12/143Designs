from abc import ABC, abstractmethod
from typing import List

from Entities.Work import Work


class WorkSALInterface(ABC):

    @abstractmethod
    def create_work(self, work: Work) -> Work:
        pass

    @abstractmethod
    def get_work(self, work_id: int) -> Work:
        pass

    @abstractmethod
    def get_all_work(self) -> List[Work]:
        pass

    @abstractmethod
    def update_work(self, work: Work) -> bool:
        pass

    @abstractmethod
    def delete_work(self, work_id: int) -> bool:
        pass
