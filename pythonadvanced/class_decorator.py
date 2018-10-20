class Decoraror1(object):

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __call__(self, *args, **kwargs):
        return Decoraror2(name=self.name,age=self.age,sex=self.sex)


class Decoraror2(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __call__(self, *args, **kwargs):
        print(self.name)
        print(self.age)
        print(self.sex)


if __name__ == "__main__":
    @Decoraror1(name=20,age=30,sex=10)
    def f():
        pass

    f()