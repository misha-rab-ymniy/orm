from orm import BaseModel


class Log(BaseModel):
    log_id: str
    date: str
    time: str
    activity_type_id: int
    user_id: int
    
    def __init__(self):
        super().__init__()