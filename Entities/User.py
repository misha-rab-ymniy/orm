from orm import BaseModel
from .Role import Role


class User(BaseModel):
    user_id: int = None
    username: str
    password: str
    role_id: int
    phone_number: str
    first_name: str
    last_name: str

    def __init__(self):
        super().__init__()

    def is_admin(self):
        try:
            isAdmin = Role().select(('name',), f"role_id = {self.role_id}")[0][0] == 'admin'
            return isAdmin
        except Exception as e:
            return False

    def is_logged(self):
        return True if self.user_id else False
