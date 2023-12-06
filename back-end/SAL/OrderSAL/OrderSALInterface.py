from abc import ABC, abstractmethod
from typing import List

from Entities.Order import Order


class OrderSALInterface(ABC):

    @abstractmethod
    def create_order(self, order: Order) -> Order:
        pass

    @abstractmethod
    def get_order(self, order_id: int) -> Order:
        pass

    @abstractmethod
    def get_all_orders(self) -> List[Order]:
        pass

    @abstractmethod
    def update_order(self, order: Order) -> bool:
        pass

    @abstractmethod
    def delete_order(self, order_id: int) -> bool:
        pass
