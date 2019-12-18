from abc import ABC, abstractmethod
import datetime


class Person(ABC):

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def get_age(self):
        pass


class Entrant(Person):

    def get_info(self):
        return self.name, self.date_of_birth, self.faculty

    def get_age(self):
        year, month, day = map(int, self.date_of_birth.split("/"))
        age = datetime.date.today() - datetime.date(year, month, day)
        return age.days // 365

    def __init__(self, name, date_of_birth, faculty):
        self.name = name
        self.date_of_birth = date_of_birth
        self.faculty = faculty


class Student(Person):

    def get_info(self):
        return self.name, self.date_of_birth, self.faculty, self.course

    def get_age(self):
        year, month, day = map(int, self.date_of_birth.split("/"))
        age = datetime.date.today() - datetime.date(year, month, day)
        return age.days // 365

    def __init__(self, name, date_of_birth, faculty, course):
        self.name = name
        self.date_of_birth = date_of_birth
        self.faculty = faculty
        self.course = course


class Teacher(Person):

    def get_info(self):
        return self.name, self.date_of_birth, self.position, self.experience

    def get_age(self):
        year, month, day = map(int, self.date_of_birth.split("/"))
        age = datetime.date.today() - datetime.date(year, month, day)
        return age.days // 365

    def __init__(self, name, date_of_birth, position, experience):
        self.name = name
        self.date_of_birth = date_of_birth
        self.position = position
        self.experience = experience


base = [Entrant("Berehovets", "1996/01/09", "Chemical"),
        Student("Kulachock", "1995/02/16", "Chemical", 3),
        Teacher("Zuy", "1974/03/13", "Professor", 20)]

for i in base:
    print(*i.get_info(), end=". ")
    print("Age is " + str(i.get_age())) if i.get_age() <= 30 else print("Age is above 30 years.")
