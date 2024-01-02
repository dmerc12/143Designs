class User:

    def __init__(self, user_id: int, email: str, password: str):
        self.user_id = user_id
        self.email = email
        self.password = password

    def convert_to_dictionary(self):
        return {
            'userId': self.user_id,
            'email': self.email
        }

    def convert_to_dictionary_full(self):
        return {
            'userId': self.user_id,
            'email': self.email,
            'password': self.password
        }
