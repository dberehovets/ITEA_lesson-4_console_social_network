from __future__ import absolute_import
from files.Base import Base
from files.User import User

b = Base()

user1 = User("dberehovets@gmail.com", "asdf12")
b.add_user(user1)