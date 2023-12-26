from Orm import BaseModel


class Cinema(BaseModel):
    cinema_id: int
    name: str
    location: str

    def __init__(self):
        super().__init__()
