import logging
from typing import List

from .modals import Item

class ItemMiddleware:

    @staticmethod
    def create_item(name: str) -> Item:
        logging.info("Beginning method create item with name: " + str(name))
        if type(name) != str:
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
                logging.info("Finishing method create item")
                return Item.objects.create(name=name)

    @staticmethod
    def get_all_items() -> List[Item]:
        items = Item.objects.all()
        if not items:
            raise RuntimeError("No items created yet")
        return items

    @staticmethod
    def get_item(item_id: int) -> Item:
        return Item.objects.get(pk=item_id)

    @staticmethod
    def update_item(item_id: int, name: str) -> bool:
        logging.info("Beginning method create item with name: " + str(name))
        if type(name) != str:
            logging.warning("Error in method create item, name not a string")
            raise RuntimeError("The name field must be a string, please try again!")
        elif len(name) > 60:
            logging.warning("Error in method create item, name too long")
            raise RuntimeError("The name field cannot exceed 60 characters, please try again!")
        elif name == "":
            logging.warning("Error in method create item, name empty")
            raise RuntimeError("The name field cannot be left empty, please try again!")
        else:
            item = ItemMiddleware.get_item(item_id)
            current_items = Item.objects.filter(name=name)
            if item.name == name:
                logging.warning("Error in method update item, nothing changed")
                raise RuntimeError("Nothing changed!")
            elif current_items:
                logging.warning("Error in method create item, item already exists")
                raise RuntimeError("This item already exists, please try again!")
            else:
                item.name = name
                item.save()
                return True

    @staticmethod
    def delete_item(item_id: int) -> bool:
        item = ItemMiddleware.get_item(item_id)
        item.delete()
        return True
