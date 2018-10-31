from datetime import date,datetime


class User:
    def __init__(self,name,birthday):
        self.name = name
        self.birthday = birthday
        self._age = None

    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self,value):
        self._age = value


if __name__ == "__main__":
    user = User('qijie',date(year=1987,month=12,day=9))
    print(user.age)
    user.age = 30
    print(user._age)