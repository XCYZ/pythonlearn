from datetime import date,datetime
import numbers

class User:
    def __init__(self,name,birthday,email):
        self.name = name
        self.birthday = birthday
        self._age = None
        self.email = email

    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self,value):
        self._age = value


class IntFiled(object):
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("value not a number")
        self.value = value

    def __delete__(self, instance):
        pass


class Module:
    pass


class User:
    age = IntFiled()


if __name__ == "__main__":
    user = User()
    user.age = 100




