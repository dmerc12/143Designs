class Item:

    def __init__(self, item_id: int, name: str):
        self.item_id = item_id
        self.name = name

    def convert_to_dictionary(self):
        return {
            'itemId': self.item_id,
            'name': self.name
        }
