import logging
from typing import List
from django.forms.models import model_to_dict

from ..models import Item

class ItemMiddleware:

    @staticmethod
    def create_item(name: str) -> Item:
        logging.info("Beginning method create item with name: " + str(name))
        if type(name) is not str:
            logging.warning("Error in method create item, name not a string")
            raise RuntimeError("The name field must be a string, please try again!")
        elif len(name) > 60:
            logging.warning("Error in method create item, name too long")
            raise RuntimeError("The name field cannot exceed 60 characters, please try again!")
        elif name == "":
            logging.warning("Error in method create item, name empty")
            raise RuntimeError("The name field cannot be left empty, please try again!")
        else:
            current_items = Item.objects.filter(name=name)
            if current_items:
                logging.warning("Error in method create item, item already exists")
                raise RuntimeError("This item already exists, please try again!")
            else:
                item = Item.objects.create(name=name)
                logging.info("Finishing method create item with item: " + item.__str__())
                return item

    @staticmethod
    def get_item(item_id: int) -> Item:
        logging.info("Beginning method get item with item ID: " + str(item_id))
        if type(item_id) is not int:
            logging.warning("Error in method get item, item ID not an integer")
            raise RuntimeError("The item ID field must be an integer, please try again!")
        else:
            item = Item.objects.get(pk=item_id)
            if not item:
                logging.warning("Error in method get item, no item found")
                raise RuntimeError("No item found, please try again!")
            else:
                logging.info("Finishing method get item with item: " + item.__str__())
                return item

    @staticmethod
    def get_all_items() -> List[Item]:
        logging.info("Beginnig method get all items")
        items = Item.objects.all()
        if not items:
            logging.warning("Error in method get all items, none found")
            raise RuntimeError("No items created yet!")
        else:
            logging.info("Finishing method get all items with items: " + str([item.__str__() for item in items]))
            return items

    @staticmethod
    def update_item(item: Item) -> bool:
        logging.info("Beginning method update item with item: " + item.__str__())
        if type(item.name) != str:
            logging.warning("Error in method update item, name not a string")
            raise RuntimeError("The name field must be a string, please try again!")
        elif len(item.name) > 60:
            logging.warning("Error in method update item, name too long")
            raise RuntimeError("The name field cannot exceed 60 characters, please try again!")
        elif item.name == "":
            logging.warning("Error in method update item, name empty")
            raise RuntimeError("The name field cannot be left empty, please try again!")
        else:
            current_item = ItemMiddleware.get_item(item.pk)
            current_items = Item.objects.filter(name=item.name)
            if current_item.name == item.name:
                logging.warning("Error in method update item, nothing changed")
                raise RuntimeError("Nothing changed!")
            elif current_items:
                logging.warning("Error in method update item, item already exists")
                raise RuntimeError("This item already exists, please try again!")
            else:
                current_item.name = item.name
                current_item.save()
                logging.info("Finishing method update item")
                return True

    @staticmethod
    def delete_item(item_id: int) -> bool:
        logging.info("Beginning method delete item with item ID: " + str(item_id))
        item = ItemMiddleware.get_item(item_id)
        item.delete()
        logging.info("Finishing method delete item")
        return True
