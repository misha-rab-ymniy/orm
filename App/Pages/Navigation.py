from .Login import LoginPage
from Entities import User, Log, ActivityType


class NavigationComponent:
    _user: User

    def __init__(self, user: User = User()):
        self._user = user

    def navigate(self):
        while True:
            print("Choose page you want to navigate to:")
            choices = {2: self.films, 1: self.exit}
            print("1. Exit\n2. Films")
            if self._user.is_logged():
                print("3. Profile\n4. Logout")
                print(f"Your nickname: {self._user.username}")
                choices[3] = self.profile
                choices[4] = self.logout
            else:
                print("3. Login")
                choices[3] = self.login
            choice = int(input())
            choices[choice]()

    def films(self):
        pass

    def exit(self):
        exit()

    def profile(self):
        print(f"Your username: {self._user.username}")
        print(f"Your password: {self._user.password}")
        print(f"Your phone number: {self._user.phone_number}")
        print(f"Your first name: {self._user.first_name}")
        print(f"Your last name: {self._user.last_name}")
        if self._user.is_admin():
            print("You are an admin")
        logs = Log().select(condition=f"user_id = {self._user.user_id}")
        print("Logs: ")
        for log in logs:
            activity_type = ActivityType().select(condition=f"activity_type_id = '{log.activity_type_id}'")[0].name
            print(
                f"{log.date}, {log.time}, {activity_type}")

    def logout(self):
        self._user = LoginPage().logout()

    def login(self):
        self._user = LoginPage().account_login()
