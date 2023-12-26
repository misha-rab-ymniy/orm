from Orm import BaseModel


class AvailableSeat(BaseModel):
    available_seat_id: int
    schedule_id: int
    seat_id: int
    available: bool

    def __init__(self):
        super().__init__()
