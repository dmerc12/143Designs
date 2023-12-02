from typing import List


class Order:

    def __init__(self, customer_name: str, item_list: List[dict], description: str, complete: bool, paid: bool):
        self.customer_name = customer_name
        self.complete = complete
        self.paid = paid
        self.description = description
        self.item_list = item_list

    def convert_to_dictionary(self):
        return {
            'customer_name': self.customer_name,
            'complete': self.complete,
            'paid': self.paid,
            'description': self.description,
            'itemList': self.item_list
        }
