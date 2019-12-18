import datetime
from files.Base import Base


class Registration:

    def register(self, email):

        self.email = email
        self.__password = input("Please create the password that contains at least 6 symbols - letters and numbers")
        self.name = input("Type your name")
        self.date_of_birth = input("Give us your date of birth in format YYYY/MM/DD")
        self.status = input("Let us know if you are married or in relationship. Type correct answer")
        self.date_of_registr = datetime.date.today()


class Login(Registration):

    def register(self, email):
        super().register(email)

    def login(self, email, password):
        if email not in Base().get_base():
            Login().register(email)
        else:
            base = Base().get_base()
            while password != base[email]["passwd"]:
                password = input("Please enter your password again")
            print("You are now in your system. Make your first post!\n")


class User(Login):

    def __init__(self, email, password):
        super().login(email, password)

    @property
    def passwd(self):
        return self.__password

    @passwd.setter
    def passwd(self, new_pass):
        self.__password = new_pass


# class Admin(User):
#     def __init__(self, email, password, name, date_of_birth, status):
#         super().__init__(email, password, name, date_of_birth, status)
#
#     @property
#     def passwd(self):
#         return super().passwd()
#
#     def show_all_users(self):
#         pass