import bcrypt


class IDGenerator:

    def __init__(self):
        self.counter = 0

    def generate_id(self) -> str:
        self.counter += 1
        hashed_id_with_salt = bcrypt.hashpw(str(self.counter).encode(), bcrypt.gensalt()).decode()
        hashed_id = hashed_id_with_salt.split("$", 1)[1]
        return hashed_id

    @staticmethod
    def generate_salt() -> str:
        return bcrypt.gensalt().decode()

    @staticmethod
    def remove_salt(hashed_id_with_salt: str):
        hashed_id = hashed_id_with_salt.split("$")[1]
        return hashed_id
