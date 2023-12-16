import logging
from typing import List

from ..models import Item, Order, OrderItem

class OrderItemMiddleware:

    @staticmethod
    def create_order_item(item: Item, order: Order, quantity: int) -> OrderItem:
        pass

    @staticmethod
    def get_order_item(order_item_id: int) -> OrderItem:
        pass

    @staticmethod
    def get_all_order_items() -> List[OrderItem]:
        pass

    @staticmethod
    def update_order_item(order_item: OrderItem) -> bool:
        pass

    @staticmethod
    def delete_order_item(order_item_id: int) -> bool:
        pass
