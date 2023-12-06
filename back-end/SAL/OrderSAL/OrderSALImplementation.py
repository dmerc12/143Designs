import logging
from typing import List

from DAL.ItemDAL.ItemDALImplementation import ItemDALImplementation
from SAL.ItemSAL.ItemSALImplementation import ItemSALImplementation
from DAL.OrderDAL.OrderDALImplementation import OrderDALImplementation
from SAL.OrderSAL.OrderSALInterface import OrderSALInterface
from Entities.CustomError import CustomError
from Entities.Order import Order


class OrderSALImplementation(OrderSALInterface):
    item_dao = ItemDALImplementation()
    item_sao = ItemSALImplementation(item_dao)

    def __init__(self, order_dao: OrderDALImplementation):
        self.order_dao = order_dao

    def create_order(self, order: Order) -> Order:
        logging.info("Beginning SAL method create order with order: " + str(order.convert_to_dictionary()))
        if type(order.customer_name) is not str:
            logging.warning("Error in SAL method create order, customer name not a string")
            raise CustomError("The customer name field must be a string, please try again!")
        elif len(order.customer_name) > 60:
            logging.warning("Error in SAL method create order, customer name too long")
            raise CustomError("The customer name field cannot exceed 60 characters, please try again!")
        elif order.customer_name == "":
            logging.warning("Error in SAL method create order, customer name left empty")
            raise CustomError("The customer name field cannot be left empty, please try again!")
        elif type(order.item_list) is not dict:
            logging.warning("Error in SAL method create order, item list not a dictionary")
            raise CustomError("The item list field must be a dictionary, please try again!")
        elif len(order.item_list) == 0:
            logging.warning("Error in SAL method create order, item list empty")
            raise CustomError("The order item list field cannot be left empty, please try again!")
        elif type(order.description) is not str:
            logging.warning("Error in SAL method create order, description not a string")
            raise CustomError("The description field must be a string, please try again!")
        elif len(order.description) > 255:
            logging.warning("Error in SAL method create order, description too long")
            raise CustomError("The description field cannot exceed 255 characters, please try again!")
        elif order.description == "":
            logging.warning("Error in SAL method create order, description left empty")
            raise CustomError("The description field cannot be left empty, please try again!")
        elif type(order.complete) is not bool:
            logging.warning("Error in SAL method create order, complete not a boolean")
            raise CustomError("The complete field must be a boolean, please try again!")
        elif type(order.paid) is not bool:
            logging.warning("Error in SAL method create order, paid not a boolean")
            raise CustomError("The paid field must be a boolean, please try again!")
        else:
            for item_id, quantity in order.item_list.items():
                if type(item_id) is not int:
                    logging.warning("Error in SAL method create order, item ID not an integer")
                    raise CustomError("The item list item ID field must be an integer, please try again!")
                elif type(quantity) is not int:
                    logging.warning("Error in SAL method create order, quantity not an integer")
                    raise CustomError("The item list quantity field must be an integer, please try again!")
                elif quantity < 1:
                    logging.warning("Error in SAL method create order, quantity negative or 0")
                    raise CustomError("The item list quantity field must be positive, please try again!")
                else:
                    self.item_sao.get_item(item_id)
            order = self.order_dao.create_order(order)
            logging.info("Finishing SAL method create order with order: " + str(order))
            return order

    def get_order(self, order_id: int) -> Order:
        logging.info("Beginning SAL method get order with order ID: " + str(order_id))
        if type(order_id) is not int:
            logging.warning("Error in SAL method get order, order ID not an integer")
            raise CustomError("The order ID field must be an integer, please try again!")
        else:
            order = self.order_dao.get_order(order_id)
            if order.order_id == 0 and order.customer_name == "" and order.item_list == {} and \
                    order.description == "" and order.complete is False and order.paid is False:
                logging.warning("Error in SAL method get order, order not found")
                raise CustomError("Order not found, please try again!")
            else:
                logging.info("Finishing SAL method get order with order: " + str(order.convert_to_dictionary()))
                return order

    def get_all_orders(self) -> List[Order]:
        logging.info("Beginning SAL method get all orders")
        orders = self.order_dao.get_all_orders()
        if len(orders) == 0:
            logging.warning("Error in SAL method get all orders, none found")
            raise CustomError("No orders found, please try again!")
        else:
            logging.info("Finishing SAL method get all orders")
            return orders

    def update_order(self, order: Order) -> bool:
        logging.info("Beginning SAL method update order with order: " + str(order.convert_to_dictionary()))
        if type(order.order_id) is not int:
            logging.warning("Error in SAL method update order, order ID not an integer")
            raise CustomError("The order ID field must be an integer, please try again!")
        elif type(order.customer_name) is not str:
            logging.warning("Error in SAL method update order, customer name not a string")
            raise CustomError("The customer name field must be a string, please try again!")
        elif len(order.customer_name) > 60:
            logging.warning("Error in SAL method update order, customer name too long")
            raise CustomError("The customer name field cannot exceed 60 characters, please try again!")
        elif order.customer_name == "":
            logging.warning("Error in SAL method update order, customer name left empty")
            raise CustomError("The customer name field cannot be left empty, please try again!")
        elif type(order.item_list) is not dict:
            logging.warning("Error in SAL method update order, item list not a dictionary")
            raise CustomError("The item list field must be a dictionary, please try again!")
        elif len(order.item_list) == 0:
            logging.warning("Error in SAL method update order, item list empty")
            raise CustomError("The order item list field cannot be left empty, please try again!")
        elif type(order.description) is not str:
            logging.warning("Error in SAL method update order, description not a string")
            raise CustomError("The description field must be a string, please try again!")
        elif len(order.description) > 255:
            logging.warning("Error in SAL method update order, description too long")
            raise CustomError("The description field cannot exceed 255 characters, please try again!")
        elif order.description == "":
            logging.warning("Error in SAL method update order, description left empty")
            raise CustomError("The description field cannot be left empty, please try again!")
        elif type(order.complete) is not bool:
            logging.warning("Error in SAL method update order, complete not a boolean")
            raise CustomError("The complete field must be a boolean, please try again!")
        elif type(order.paid) is not bool:
            logging.warning("Error in SAL method update order, paid not a boolean")
            raise CustomError("The paid field must be a boolean, please try again!")
        else:
            self.get_order(order.order_id)
            for item_id, quantity in order.item_list.items():
                if type(item_id) is not int:
                    logging.warning("Error in SAL method update order, item ID not an integer")
                    raise CustomError("The item list item ID field must be an integer, please try again!")
                elif type(quantity) is not int:
                    logging.warning("Error in SAL method update order, quantity not an integer")
                    raise CustomError("The item list quantity field must be an integer, please try again!")
                elif quantity < 1:
                    logging.warning("Error in SAL method update order, quantity negative or 0")
                    raise CustomError("The item list quantity field must be positive, please try again!")
                else:
                    self.item_sao.get_item(item_id)
            result = self.order_dao.update_order(order)
            logging.info("Finishing SAL method update order")
            return result

    def delete_order(self, order_id: int) -> bool:
        logging.info("Beginning SAL method delete order with order ID: " + str(order_id))
        if type(order_id) is not int:
            logging.warning("Error in SAL method delete order, order ID not an integer")
            raise CustomError("The order ID field must be an integer, please try again!")
        else:
            self.get_order(order_id)
            result = self.order_dao.delete_order(order_id)
            logging.info("Finishing SAL method delete order")
            return result
