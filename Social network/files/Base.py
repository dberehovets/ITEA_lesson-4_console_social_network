import datetime


class Base:

    base = {}
    content_base = {}

    def add_user(self, user):
        self.base[user.email] = {
            "name": user.name,
            "birth": user.date_of_birth,
            "status": user.status,
            "passwd": user.passwd,
            "reg_date": user.date_of_registr
        }

    def get_base(self):
        return self.base

    def add_content(self, user, content):
        if user.email in self.content_base:
            a = self.content_base[user.email]
            a[datetime.datetime.now()] = content
        else:
            self.content_base[user.email] = {
                datetime.datetime.now(): content
        }

    def get_content(self):
        return self.content_base
