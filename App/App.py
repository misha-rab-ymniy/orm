from Entities import User
from .Pages import LoginPage, NavigationComponent


class App:
    _user: User = None

    def __init__(self):
        # login_page = LoginPage()
        # login_page.account_login()
        # self._user = login_page.get_user()
        navigation = NavigationComponent()
        self._user = navigation.navigate()

