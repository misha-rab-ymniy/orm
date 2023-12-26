from Orm import BaseModel


class Ticket(BaseModel):
    ticket_id: int
    user_id: int
    date_of_purchase: str
    schedule_id: int
    seat_id: int

    def __init__(self):
        super().__init__()
