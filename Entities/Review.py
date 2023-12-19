from Orm import BaseModel


class Review(BaseModel):
    review_id: int
    film_id: int
    user_id: int
    text: str

    def __init__(self):
        super().__init__()
