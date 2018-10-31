#__getattr__,__getattribute__
#__getattr__在查找不到属性时候使用
from datetime import datetime,date

class User:
    def __init__(self,name,birthday):
        self.name = name
        self.birthday = birthday

    def __getattr__(self, item):
        return "not find attr"

    def __getattribute__(self, item):
        return "sbsbsbsb"


if __name__ == "__main__":
    user = User('sb',date(2000,12,12))
    print(user.name)
    print(user.age)
