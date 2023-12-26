from Orm import BaseModel


class Hall(BaseModel):
    hall_id: int
    capacity: int
    hall_name: str
    cinema_id: int

    def __init__(self):
        super().__init__()
