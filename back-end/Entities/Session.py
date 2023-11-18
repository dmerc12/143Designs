from datetime import datetime

class Session:

    def __init__(self, session_id: int, user_id: int, expiration: datetime):
        self.session_id = session_id
        self.user_id = user_id
        self.expiration = expiration

    def convert_to_dictionary(self):
        return {
            'sessionId': self.session_id,
            'userId': self.user_id,
            'expiration': self.expiration
        }
