from Orm import BaseModel


class Genre(BaseModel):
    genre_id: str
    name: str

    def __init__(self):
        super().__init__()
