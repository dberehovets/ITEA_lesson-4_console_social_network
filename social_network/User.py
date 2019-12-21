import datetime
from Base import Base

class Registration:

    @staticmethod
    def register(email):

        print("Hi! We don't know you... Please follow the instructions below to register in the system")
        email = email
        _password = input("Please create the password that contains at least 6 symbols - letters and numbers\n")
        name = input("Type your name\n")
        date_of_birth = input("Give us your date of birth in format YYYY/MM/DD\n")
        status = input("Let us know if you are married or in relationship. Type correct answer\n")
        date_of_registr = datetime.date.today()
        admin = Base().get_base() == {}
        dc = {
            "email": email,
            "passwd": _password,
            "name": name,
            "date_of_birth": date_of_birth,
            "status": status,
            "reg_date": date_of_registr,
            "admin": admin
        }

        Base().add_user(**dc)


class Login(Registration):

    @staticmethod
    def login(email):
        if email not in Base().get_base():
            Login().register(email)
        else:
            password = input("Hello! Please fill in the password\n")
            base = Base().get_base()
            while password != base[email]["passwd"]:
                password = input("Please enter your password again")
            print("You are now in the system. What are we doing next?")


class User(Login):
    b = Base()

    def __init__(self, email):
        self.email = email
        super().login(email)

    def what_to_do(self):
        while True:
            choice = input("""Please choose what you would like to do further:
            type 'new post' if you want to make some post
            type 'info' if you would like to see information about yourself
            type 'show posts'
            type '0' to exit\n""")
            if choice == "new post":
                self.make_post()
            elif choice == "info":
                self.show_info_about_me()
            elif choice == "show posts":
                self.show_my_posts()
            elif choice == "0":
                break

    def make_post(self):
        text = input("Please let us know what you think\n")
        self.b.add_content(self.email, text)

    def show_my_posts(self):
        content = self.b.get_content(self.email)
        for i in reversed(content):
            print(i.date(), content[i])

    def show_info_about_me(self):
        info = self.b.get_someone_info(self.email)
        for i in info:
            print(i, ":", info[i])


class Admin(User):

    def what_to_do(self):
        while True:
            choice = input("""Please choose what you would like to do further:
            type 'new post' to make some post
            type 'info' to see information about yourself
            type 'show posts' to see your posts
            type 'show users' to see all users and their posts
            type 'clear' to clear database
            type '0' to exit\n""")
            if choice == "new post":
                self.make_post()
            elif choice == "delete":
                self.clear_data()
            elif choice == "info":
                self.show_info_about_me()
            elif choice == "show posts":
                self.show_my_posts()
            elif choice == "show users":
                self.show_all_users()
            elif choice == "0":
                break

    def show_all_users(self):
        info = self.b.get_base()
        for i in info:
            content = self.b.get_content(info[i]["email"])
            print(info[i]["name"], "registered", info[i]["reg_date"])
            try:
                for j in reversed(content):
                    print(j.date(), content[j])
            except AttributeError:
                print("No posts")
            print("")

    def clear_data(self):
        self.b.clear_base()
        self.b.clear_content()
