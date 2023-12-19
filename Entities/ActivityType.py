from Orm import BaseModel


class ActivityType(BaseModel):
    activity_type_id: int
    name: str

    def __init__(self):
        super().__init__()
