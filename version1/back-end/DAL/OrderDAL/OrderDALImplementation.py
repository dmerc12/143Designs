import json
import logging
from typing import List

from DAL.OrderDAL.OrderDALInterface import OrderDALInterface
from Database.DBConnection import DBConnection
from Entities.Order import Order


class OrderDALImplementation(OrderDALInterface):

    def create_order(self, order: Order) -> Order:
        logging.info("Beginning DAL method create order with order: " + str(order.convert_to_dictionary()))
        sql = "INSERT INTO Designs.Order (customer_name, item_list, description, complete, paid) " \
              "VALUES (%s, %s, %s, %s, %s) RETURNING order_id;"
        connection = DBConnection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (order.customer_name, json.dumps(order.item_list), order.description, order.complete,
                             order.paid))
        order.order_id = cursor.fetchone()[0]
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method create order with order: " + str(order.convert_to_dictionary()))
        return order

    def get_order(self, order_id: int) -> Order:
        logging.info("Beginning DAL method get order with order ID: " + str(order_id))
        sql = "SELECT * FROM Designs.Order WHERE order_id=%s;"
        connection = DBConnection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (order_id,))
        order_info = cursor.fetchone()
        cursor.close()
        if order_info is None:
            order = Order(0, "", {}, "", False, False)
            logging.warning("Finishing DAL method get order, order not found")
            return order
        else:
            order = Order(*order_info)
            logging.info("Finishing DAL method get order with order: " + str(order.convert_to_dictionary()))
            return order

    def get_all_orders(self) -> List[Order]:
        logging.info("Beginning DAL method get all orders")
        sql = "SELECT * FROM Designs.Order;"
        connection = DBConnection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql)
        order_records = cursor.fetchall()
        cursor.close()
        connection.close()
        order_list = []
        for order in order_records:
            order = Order(*order)
            order_list.append(order)
            logging.info("Finishing DAL method get all orders with orders: " + str(order.convert_to_dictionary()))
        return order_list

    def update_order(self, order: Order) -> bool:
        logging.info("Beginning DAL method update order with order: " + str(order.convert_to_dictionary()))
        sql = "UPDATE Designs.Order SET customer_name=%s, item_list=%s, description=%s, complete=%s " \
              "AND paid=%s WHERE order_id=%s;"
        connection = DBConnection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (order.customer_name, json.dumps(order.item_list), order.description, order.complete,
                             order.paid, order.order_id))
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method update order")
        return True

    def delete_order(self, order_id: int) -> bool:
        logging.info("Beginning DAL method delete order with order ID: " + str(order_id))
        sql = "DELETE FROM Designs.Order WHERE order_id=%s;"
        connection = DBConnection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (order_id,))
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method delete order")
        return True
