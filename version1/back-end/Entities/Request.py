from datetime import datetime, date

class Request:

    # company name will be optional
    def __init__(self, request_id: int, first_name: str, last_name: str, company_name: str, email: str,
                 phone_number: str, message: str, completion_date: date, complete: bool, timestamp: datetime):
        self.request_id = request_id
        self.first_name = first_name
        self.last_name = last_name
        self.company_name = company_name
        self.email = email
        self.phone_number = phone_number
        self.message = message
        self.completion_date = completion_date
        self.complete = complete
        self.timestamp = timestamp

    def convert_to_dictionary(self):
        if self.company_name:
            return {
                'requestId': self.request_id,
                'firstName': self.first_name,
                'lastName': self.last_name,
                'companyName': self.company_name,
                'email': self.email,
                'phoneNumber': self.phone_number,
                'message': self.message,
                'complete': self.complete,
                'timestamp': self.timestamp
            }
        else:
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
