from __future__ import absolute_import
from User import User, Admin
from Base import Base

while True:
    email = input("Welcome to Yourbook! Please enter your email below or type 0 to exit:\n")
    if email == "0":
        break
    try:
        admin = Base().get_base()[email]["admin"]
    except KeyError:
        admin = False

    if Base().get_base() == {} or admin != False:
        user = Admin(email)
        user.what_to_do()
    else:
        user = User(email)
        user.what_to_do()
