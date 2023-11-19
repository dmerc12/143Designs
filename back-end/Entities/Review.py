class Review:

    def __init__(self, review_id: int, first_name: str, last_name: str, text: str, rating: float):
        self.review_id = review_id
        self.first_name = first_name
        self.last_name = last_name
        self.text = text
        self.rating = rating

    def convert_to_dictionary(self):
        return {
            'reviewId': self.review_id,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'text': self.text,
            'rating': self.rating,
        }
