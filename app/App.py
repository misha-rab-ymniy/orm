from Entities import User
from .pages import LoginPage


class App:
    _user: User = None

    def __init__(self):
        login_page = LoginPage()
        self._user = login_page.get_user()

