from orm import BaseModel


class Role(BaseModel):
    role_id: str
    name: str

    def __init__(self):
        super().__init__()
