import logging
from typing import List
from django.forms.models import model_to_dict
from django.core.exceptions import ValidationError

from ..models import Item, Order, OrderItem
from ..item.middleware import ItemMiddleware
from ..order.middleware import OrderMiddleware

class OrderItemMiddleware:

    @staticmethod
    def create_order_item(order: Order, item: Item, quantity: int) -> OrderItem:
        logging.info("Beginning method create order-item with order: " + order.__str() + ", item: " + item.__str__() + ", quantity: " + str(quantity))
        if type(order) is not Order:
            logging.warning("Error in method create order-item, order not an order")
            raise ValidationError("The order field must be an order, please try again!")
        elif type(item) is not Item:
            logging.warning("Error in method create order-item, item not an item")
            raise ValidationError("The item field must be an item, please try again!")
        elif type(quantity) is not int:
            logging.warning("Error in method create order-item, quantity not an integer")
            raise ValidationError("The quantity field must be an integer, please try again!")
        elif quantity < 0:
            logging.warning("Error in method create order-item, quanatity negative")
            raise ValidationError("The quatity field must be positive, please try again!")
        else:
            OrderMiddleware.get_order(order.pk)
            ItemMiddleware.get_order(item.pk)
            order_item = OrderItem.objects.create(order=order, item=item, quantity=quantity)
            logging.info("Finishing method create order-item with order-item: " + order_item.__str__())
            return order_item

    @staticmethod
    def get_order_item(order_item_id: int) -> OrderItem:
        logging.info("Beginning method get order-item with order-item ID: " + str(order_item_id))
        if type(order_item_id) is not int:
            logging.warning("Error in method get order-item, order-item ID not an integer")
            raise ValidationError("The order-item ID field must be an integer")
        else:
            order_item = OrderItem.objects.get(pk=order_item_id)
            if not order_item:
                logging.warning("Error in method get order-item, no order-item found")
                raise ValidationError("No order-item found, please try again!")
            else:
                logging.info("Finishing method get order-item with order-item: " + order_item.__str())
                return order_item

    @staticmethod
    def get_all_order_items() -> List[OrderItem]:
        logging.info("Beginning method get all order-items")
        order_items = OrderItem.objects.all()
        if not order_items:
            logging.warning("Error in method get all order-items, none found")
            raise ValidationError("no order-items created yet!")
        else:
            logging.info("Finishing method get all order-items with order-items: " + order_item.__str__() for order_item in order_items)
            return order_items

    @staticmethod
    def update_order_item(order_item: OrderItem) -> bool:
        logging.info("Beginning method update order-item with order: " + order_item.order.__str() + ", item: " + order_item.item.__str__() + ", quantity: " + str(order_item.quantity))
        if type(order_item.order) is not Order:
            logging.warning("Error in method update order-item, order not an order")
            raise ValidationError("The order field must be an order, please try again!")
        elif type(order_item.item) is not Item:
            logging.warning("Error in method update order-item, item not an item")
            raise ValidationError("The item field must be an item, please try again!")
        elif type(order_item.quantity) is not int:
            logging.warning("Error in method update order-item, quantity not an integer")
            raise ValidationError("The quantity field must be an integer, please try again!")
        elif order_item.quantity < 0:
            logging.warning("Error in method update order-item, quanatity negative")
            raise ValidationError("The quatity field must be positive, please try again!")
        else:
            current_order_item = OrderItemMiddleware.get_order_item(order_item.pk)
            OrderMiddleware.get_order(order_item.order.pk)
            ItemMiddleware.get_order(order_item.item.pk)
            if model_to_dict(current_order_item) == model_to_dict(order_item):
                logging.warning("Error in method update order-item, nothing changed")
                raise ValidationError("Nothing changed!")
            else:
                current_order_item.order = order_item.order
                current_order_item.item = order_item.item
                current_order_item.quantity = order_item.quantity
                current_order_item.save()
                logging.info("Finishing method update order-item with order-item: " + order_item.__str__())
                return order_item

    @staticmethod
    def delete_order_item(order_item_id: int) -> bool:
        logging.info("Beginning method delete order-item with order-item ID: " + str(order_item_id))
        order_item = OrderItemMiddleware.get_order_item(order_item_id)
        order_item.delete()
        logging.info("Finishing method delete order-item")
        return True
