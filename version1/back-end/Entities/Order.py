import json


class Order:

    def __init__(self, order_id: int, customer_name: str, item_list: json, description: str, complete: bool,
                 paid: bool):
        self.order_id = order_id
        self.customer_name = customer_name
        self.item_list = item_list
        self.description = description
        self.complete = complete
        self.paid = paid

    def convert_to_dictionary(self):
        return {
            'orderId': self.order_id,
            'customerName': self.customer_name,
            'itemList': self.item_list,
            'description': self.description,
            'complete': self.complete,
            'paid': self.paid,
        }
