from typing import List

from DAL.OrderDAL.OrderDALImplementation import OrderDALImplementation
from SAL.OrderSAL.OrderSALInterface import OrderSALInterface
from Entities.Order import Order


class OrderSALImplementation(OrderSALInterface):

    def __init__(self, order_dao: OrderDALImplementation):
        self.order_dao = order_dao

    def create_order(self, order: Order) -> Order:
        pass

    def get_order(self, order_id: int) -> Order:
        pass

    def get_all_orders(self) -> List[Order]:
        pass

    def update_order(self, order: Order) -> bool:
        pass

    def delete_order(self, order_id: int) -> bool:
        pass
