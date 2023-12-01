class Work:

    def __init__(self, work_id: int, name: str, description: str):
        self.work_id = work_id
        self.name = name
        self.description = description

    def convert_to_dictionary(self):
        return {
            'workId': self.work_id,
            'name': self.name,
            'description': self.description,
        }
