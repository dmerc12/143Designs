import logging
from typing import List
from django.forms.models import model_to_dict
from django.core.exceptions import ValidationError

from ..models import Order

class OrderMiddleware:

    @staticmethod
    def create_order(name: str, description: str, complete: bool, paid: bool) -> Order:
        logging.info("Beginning method create order with name: " + str(name) + ", description: " + str(description) + ", complete: " + str(complete) + ", paid: " + str(paid))
        if type(name) is not str:
            logging.warning("Error in method create order, name not a string")
            raise ValidationError("The name field must be a string, please try again!")
        elif len(name) > 60:
            logging.warning("Error in method create order, name too long")
            raise ValidationError("The name field exceed 60 characters, please try again!")
        elif name == "":
            logging.warning("Error in method create order, name left empty")
            raise ValidationError("The name field cannot be left empty, please try again!")
        elif type(description) is not str:
            logging.warning("Error in method create order, description not a string")
            raise ValidationError("The description field must be a sting, please try again!")
        elif len(description) > 255:
            logging.warning("Error in method create order, description too long")
            raise ValidationError("The description field cannot exceed 255 characters, please try again!")
        elif description == "":
            logging.warning("Error in method create order, description left empty")
            raise ValidationError("The description field cannot be left empty, please try again!")
        elif type(complete) is not bool:
            logging.warning("Error in method create order, complete not a boolean")
            raise ValidationError("The complete field must be a boolean, please try again!")
        elif type(paid) is not bool:
            logging.warning("Error in method create order, paid not a boolean")
            raise ValidationError("The paid field must be a boolean, please try again!")
        else:
            order = Order.objects.create(name=name, description=description, complete=complete, paid=paid)
            logging.info("Finishing method create order with order: " + order.__str__())
            return order

    @staticmethod
    def get_order(order_id: int) -> Order:
        logging.info("Beginning method get order with order ID: " + str(order_id))
        if type(order_id) is not int:
            logging.warning("Error in method get order, order ID not an integer")
            raise ValidationError("The order ID field must be an integer, please try again!")
        else:
            order = Order.objects.get(pk=order_id)
            if not order:
                logging.warning("Error in method get order, no order found")
                raise ValidationError("No order found, please try again!")
            else:
                logging.info("Finishing method get order with order: " + order.__str__())
                return order

    @staticmethod
    def get_all_orders() -> List[Order]:
        logging.info("Beginning method get all orders")
        orders = Order.objects.all()
        if not orders:
            logging.warning("Error in method get all orders, none found")
            raise ValidationError("No orders created yet!")
        else:
            logging.info("Finishing method get all objects with orders: " + order.__str__() for order in orders)
            return orders

    @staticmethod
    def update_order(order: Order) -> bool:
        logging.info("Beginning method update order with order: " + order.__str__())
        if type(order.name) is not str:
            logging.warning("Error in method update order, name not a string")
            raise ValidationError("The name field must be a string, please try again!")
        elif len(order.name) > 60:
            logging.warning("Error in method update order, name too long")
            raise ValidationError("The name field exceed 60 characters, please try again!")
        elif order.name == "":
            logging.warning("Error in method update order, name left empty")
            raise ValidationError("The name field cannot be left empty, please try again!")
        elif type(order.description) is not str:
            logging.warning("Error in method update order, description not a string")
            raise ValidationError("The description field must be a sting, please try again!")
        elif len(order.description) > 255:
            logging.warning("Error in method update order, description too long")
            raise ValidationError("The description field cannot exceed 255 characters, please try again!")
        elif order.description == "":
            logging.warning("Error in method update order, description left empty")
            raise ValidationError("The description field cannot be left empty, please try again!")
        elif type(order.complete) is not bool:
            logging.warning("Error in method update order, complete not a boolean")
            raise ValidationError("The complete field must be a boolean, please try again!")
        elif type(order.paid) is not bool:
            logging.warning("Error in method update order, paid not a boolean")
            raise ValidationError("The paid field must be a boolean, please try again!")
        else:
            current_order = OrderMiddleware.get_order(order.pk)
            if model_to_dict(current_order) == model_to_dict(order):
                logging.warning("Error in method update order, nothing changed")
                raise ValidationError("Nothing changed!")
            else:
                current_order.name = order.name
                current_order.description = order.description
                current_order.complete = order.complete
                current_order.paid = order.paid
                current_order.save()
                logging.info("Finishing method update order")
                return True

    @staticmethod
    def delete_order(order_id: int) -> bool:
        logging.info("Beginning method delete order with order ID: " + str(order_id))
        order = OrderMiddleware.get_order(order_id)
        order.delete()
        logging.info("Finishing method delete order")
        return True
