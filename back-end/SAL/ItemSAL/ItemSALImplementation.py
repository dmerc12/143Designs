import logging
from typing import List

from DAL.ItemDAL.ItemDALImplementation import ItemDALImplementation
from Entities.CustomError import CustomError
from Entities.Item import Item
from SAL.ItemSAL.ItemSALInterface import ItemSALInterface


class ItemSALImplementation(ItemSALInterface):

    def __init__(self, item_dao: ItemDALImplementation):
        self.item_dao = item_dao

    def create_item(self, item: Item) -> Item:
        logging.info("Beginning SAL method create item with item: " + str(item.convert_to_dictionary()))
        if type(item.item_name) is not str:
            logging.warning("Error in SAL method create item, item name not a string")
            raise CustomError("The item name field must be a string, please try again!")
        elif len(item.item_name) > 60:
            logging.warning("Error in SAL method create item, item name too long")
            raise CustomError("The item name field cannot exceed 60 characters, please try again!")
        elif item.item_name == "":
            logging.warning("Error in SAL method create item, item name empty")
            raise CustomError("The item name field cannot be left empty, please try again!")
        else:
            current_items = self.item_dao.get_all_items()
            for current_item in current_items:
                if current_item.item_name == item.item_name:
                    logging.warning("Error in SAL method update item, item already exists")
                    raise CustomError("Item already exists, please try again!")
            item = self.item_dao.create_item(item)
            logging.info("Finishing SAL method create item with item: " + str(item))
            return item

    def get_item(self, item_id: int) -> Item:
        logging.info("Beginning SAL method get item with item ID: " + str(item_id))
        if type(item_id) is not int:
            logging.warning("Error in SAL method get item, item ID not an integer")
            raise CustomError("The item ID field must be an integer, please try again!")
        else:
            item = self.item_dao.get_item(item_id)
            if item.item_id == 0 and item.item_name == "":
                logging.warning("Error in SAL method get item, item not found")
                raise CustomError("Item not found, please try again!")
            else:
                logging.info("Finishing SAL method get item with item: " + str(item.convert_to_dictionary()))
                return item

    def get_all_items(self) -> List[Item]:
        logging.info("Beginning SAL method get all items")
        items = self.item_dao.get_all_items()
        if len(items) == 0:
            logging.warning("Error in SAL method get all items, none found")
            raise CustomError("No items found, please try again!")
        else:
            logging.info("Finishing SAL method get all items")
            return items

    def update_item(self, item: Item) -> bool:
        logging.info("Beginning SAL method update item with item: " + str(item.convert_to_dictionary()))
        if type(item.item_id) is not int:
            logging.warning("Error in SAL method update item, item ID not an integer")
            raise CustomError("The item ID field must be an integer, please try again!")
        elif type(item.item_name) is not str:
            logging.warning("Error in SAL method update item, item name not a string")
            raise CustomError("The item name field must be a string, please try again!")
        elif len(item.item_name) > 60:
            logging.warning("Error in SAL method update item, item name too long")
            raise CustomError("The item name field cannot exceed 60 characters, please try again!")
        elif item.item_name == "":
            logging.warning("Error in SAL method update item, item name empty")
            raise CustomError("The item name field cannot be left empty, please try again!")
        else:
            current_item = self.get_item(item.item_id)
            if current_item.item_name == item.item_name:
                logging.warning("Error in SAL method update item, nothing changed")
                raise CustomError("Nothing changed, please try again!")
            else:
                current_items = self.item_dao.get_all_items()
                for current_item in current_items:
                    if current_item.item_name == item.item_name:
                        logging.warning("Error in SAL method update item, item already exists")
                        raise CustomError("Item already exists, please try again!")
                result = self.item_dao.update_item(item)
                logging.info("Finishing SAL method update item")
                return result

    def delete_item(self, item_id: int) -> bool:
        logging.info("Beginning SAL method delete item with item ID: " + str(item_id))
        if type(item_id) is not int:
            logging.warning("Error in SAL method delete item, item ID not an integer")
            raise CustomError("The item ID field must be an integer, please try again!")
        else:
            self.get_item(item_id)
            result = self.item_dao.delete_item(item_id)
            logging.info("Finishing SAL method delete item")
            return result
