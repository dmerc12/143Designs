class Review:

    def __init__(self, review_id: int, name: str, text: str, rating: float):
        self.review_id = review_id
        self.name = name
        self.text = text
        self.rating = rating

    def convert_to_dictionary(self):
        return {
            'reviewId': self.review_id,
            'name': self.name,
            'text': self.text,
            'rating': self.rating,
        }
