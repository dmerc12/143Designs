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
            if current_items.exists():
                logging.warning("Error in method create item, item already exists")
                raise RuntimeError("This item already exists, please try again!")
            else:
                logging.info("Finishing method create item")
                return Item.objects.create(name=name)

    @staticmethod
    def get_all_items() -> List[Item]:
        return Item.objects.all()

    @staticmethod
    def get_item(item_id: int) -> Item:
        return Item.objects.get(item_id)

    def update_item(self, item_id: int, name: str) -> bool:
        item = self.get_item(item_id)
        item.name = name
        item.save()
        return True

    def delete_item(self, item_id: int) -> bool:
        item = self.get_item(item_id)
        item.delete()
        return True
