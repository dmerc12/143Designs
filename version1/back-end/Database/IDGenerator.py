import bcrypt


class IDGenerator:

    def __init__(self):
        self.counter = 0

    def generate_id(self) -> str:
        self.counter += 1
        hashed_id = bcrypt.hashpw(str(self.counter).encode(), bcrypt.gensalt()).decode()
        return hashed_id
