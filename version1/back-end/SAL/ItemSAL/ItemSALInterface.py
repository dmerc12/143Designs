from abc import ABC, abstractmethod
from typing import List

from Entities.Item import Item


class ItemSALInterface(ABC):

    @abstractmethod
    def create_item(self, item: Item) -> Item:
        pass

    @abstractmethod
    def get_item(self, item_id: int) -> Item:
        pass

    @abstractmethod
    def get_all_items(self) -> List[Item]:
        pass

    @abstractmethod
    def update_item(self, item: Item) -> bool:
        pass

    @abstractmethod
    def delete_item(self, item_id: int) -> bool:
        pass
