class Item:

    def __init__(self, item_id: int, item_name: str):
        self.item_id = item_id
        self.item_name = item_name

    def convert_to_dictionary(self):
        return {
            'itemId': self.item_id,
            'name': self.item_name
        }
