from Orm import BaseModel


class Film(BaseModel):
    film_id: int
    title: str
    release_date: str
    country: str
    duration: str
    description: str
    rating: int

    def __init__(self):
        super().__init__()
