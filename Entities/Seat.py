from Orm import BaseModel


class Seat(BaseModel):
    seat_id: int
    hall_id: int
    seat_number: int
    row_number: int

    def __init__(self):
        super().__init__()
