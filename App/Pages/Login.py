from Entities import User
from Entities import Role
import psycopg2.errors


class LoginPage:
    _user: User = User()
    _isSuccess: bool = False

    def __init__(self):
        pass

    def account_login(self):
        while not self._isSuccess:
            print("Do you want to signin or signup or exit(input 1/2/3)?")
            choice = input()
            if choice == "1":
                self.login()
            elif choice == "2":
                self.signup()
            elif choice == "3":
                break
            else:
                print("Invalid value. Try again...")
        return self._user

    def login(self):
        while True:
            print("Logging in...")
            print("Enter your username: ")
            username = input()
            print("Enter your password: ")
            password = input()
            try:
                self._user = self._user.select(condition=f"username = '{username}' AND password = '{password}'")[0]
                self._isSuccess = True
                break
            except IndexError:
                self._isSuccess = False
                print("Invalid username or password. Try again...")

        print("Logged in...")

    def signup(self):
        print("Signing up...")
        values = []
        print("Enter your username: ")
        values.append(input())
        print("Enter your password: ")
        values.append(input())
        role = Role().select(condition=f"name = 'user'")[0]
        values.append(role.role_id)
        print("Enter your phone_number: ")
        values.append(input())
        print("Enter your first_name: ")
        values.append(input())
        print("Enter your last_name: ")
        values.append(input())
        try:
            self._user.insert(tuple(values))
            print("Signed up...")
            self._user = self._user.select(condition=f"username = '{values[0]}'")[0]
            self._isSuccess = True
        except psycopg2.errors.CheckViolation as ex:
            print("Invalid input. Try again...")
            self._isSuccess = False

    def get_user(self):
        return self._user

    def logout(self):
        return User()
