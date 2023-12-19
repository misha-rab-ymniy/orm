from Orm import BaseModel


class FilmGenres(BaseModel):
    id: int
    genre_id: int
    film_id: int

    def __init__(self):
        super().__init__()
