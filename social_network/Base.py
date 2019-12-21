import datetime
import shelve


class Base:
    __base = {}
    __content_base = {}
    __UBASENAME = "users_base"
    __CBASENAME = "content_base"

    def add_user(self, **kwargs):
        with shelve.open(self.__UBASENAME) as states:
            states[kwargs["email"]] = kwargs

    def get_base(self):
        with shelve.open(self.__UBASENAME) as states:
            self.__base = dict(states.items())
            return self.__base

    def get_someone_info(self, email):
        with shelve.open(self.__UBASENAME) as states:
            content = states.get(email, None)
            self.__base = dict(content) if content else "No information"
            return self.__base

    def clear_base(self):
        with shelve.open(self.__UBASENAME) as st:
            st.clear()
            st.close()

    def add_content(self, email, content):
        with shelve.open(self.__CBASENAME) as states:
            if email in states:
                a = states.get(email)
                a[datetime.datetime.now()] = content
                states[email] = a
            else:
                states[email] = {
                    datetime.datetime.now(): content
                }

    def get_content(self, email):
        with shelve.open(self.__CBASENAME) as states:
            content = states.get(email, None)
            self.__content_base = dict(content) if content else "No posts"
            return self.__content_base

    def delete_user(self, email):
        with shelve.open(self.__UBASENAME) as st:
            st.pop(email)
        with shelve.open(self.__CBASENAME) as st:
            st.pop(email)

    def clear_content(self):
        with shelve.open(self.__CBASENAME) as st:
            st.clear()


# b = Base()
# print(b.get_base())
# print(b.get_content("dberehovets@gmail.com"))