import logging
from typing import List

from DAL.ItemDAL.ItemDALInterface import ItemDALInterface
from Database.DBConnection import DBConnection
from Entities.Item import Item


class ItemDALImplementation(ItemDALInterface):

    def create_item(self, item: Item) -> Item:
        logging.info("Beginning DAL method create item with item: " + str(item))
        sql = "INSERT INTO Designs.Item (item_name) VALUES (%s) RETURNING item_id;"
        connection = DBConnection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (item.name,))
        item.item_id = cursor.fetchone()[0]
        cursor.close()
        connection.commit()
        connection.close()
        logging.info("Finishing DAL method create item with item: " + str(item))
        return item

    def get_item(self, item_id: int) -> Item:
        logging.info("Beginning DAL method get item with item ID: " + str(item_id))
        sql = "SELECT * FROM Designs.Item WHERE item_id=%s;"
        connection = DBConnection.db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (item_id,))
        item_info = cursor.fetchall()
        if item_info is not None:
            item = Item(*item_info)
            logging.info("Finishing DAL method get item with item: " + str(item.convert_to_dictionary()))
            return item
        else:
            item = Item(0, "")
            logging.info("Finishing DAL method get item, item not found")
            return item

    def get_all_items(self) -> List[Item]:
        pass

    def update_item(self, item: Item) -> bool:
        pass

    def delete_item(self, item_id: int) -> bool:
        pass
