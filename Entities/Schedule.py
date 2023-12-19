from Orm import BaseModel


class Schedule(BaseModel):
    schedule_id: int
    film_id: int
    hall_id: int
    start_time: str
    value: int

    def __init__(self):
        super().__init__()
