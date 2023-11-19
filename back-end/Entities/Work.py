class Work:

    def __init__(self, work_id: int, first_name: str, last_name: str, description: str):
        self.work_id = work_id
        self.first_name = first_name
        self.last_name = last_name
        self.description = description

    def convert_to_dictionary(self):
        return {
            'workId': self.work_id,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'description': self.description,
        }
