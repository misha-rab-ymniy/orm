from .Login import LoginPage
from .Film import FilmPage
from Entities import User, Log, ActivityType, Review


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
                print("3. Profile\n4. Logout\n5. Make review")
                print(f"Your nickname: {self._user.username}")
                choices[3] = self.profile
                choices[4] = self.logout
                choices[5] = self.review
            else:
                print("3. Login")
                choices[3] = self.login
            choice = int(input())
            choices[choice]()

    def review(self):
        values = []
        print(f"Enter film_id")
        values.append(int(input()))
        values.append(self._user.user_id)
        print(f"Enter text of review")
        values.append(input())
        Review().insert(tuple(values))

    def films(self):
        film_page = FilmPage(self._user)
        film_page.film_list()
        if self._user.is_admin():
            film_page.film_change()
        film_page.took_place()

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
        print("Do you want to update your data? (y/n)")
        choice = input()
        if choice == "y":
            print(f"Enter which attribute you want to update: ")
            attribute = input()
            print(f"Enter a new value of {attribute}:")
            value = input()
            self._user.update({attribute: value}, condition=f"user_id = '{self._user.user_id}'")
            self._user = self._user.select(condition=f"user_id = '{self._user.user_id}'")[0]

    def logout(self):
        self._user = LoginPage().logout()

    def login(self):
        self._user = LoginPage().account_login()
