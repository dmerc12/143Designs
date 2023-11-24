class Order:

    def __init__(self, customer_name: str, item_id: int, description: str, complete: bool, paid: bool):
        self.customer_name = customer_name
        self.complete = complete
        self.paid = paid
        self.item_id = item_id
        self.description = description

    def convert_to_dictionary(self):
        return {
            'customer_name': self.customer_name,
            'complete': self.complete,
            'paid': self.paid,
            'itemId': self.item_id,
            'description': self.description
        }
