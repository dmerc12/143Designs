from datetime import datetime

class Request:

    def __init__(self, request_id: int, first_name: str, last_name: str, email: str, phone_number: str, message: str,
                 complete: bool, timestamp: datetime):
        self.request_id = request_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.message = message
        self.complete = complete
        self.timestamp = timestamp

    def convert_to_dictionary(self):
        return {
            'requestId': self.request_id,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'email': self.email,
            'phoneNumber': self.phone_number,
            'message': self.message,
            'complete': self.complete,
            'timestamp': self.timestamp
        }
