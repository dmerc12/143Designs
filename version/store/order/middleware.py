import logging
from typing import List

from ..models import Order

class OrderMiddleware:

    @staticmethod
    def create_order() -> Order:
        pass

    @staticmethod
    def get_order(order_id: int) -> Order:
        pass

    @staticmethod
    def get_all_orders() -> List[Order]:
        pass

    @staticmethod
    def update_order(order: Order) -> bool:
        pass

    @staticmethod
    def delete_order(order_id: int) -> bool:
        pass
