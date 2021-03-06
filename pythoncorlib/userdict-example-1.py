from UserDict import UserDict


class FancyDict(UserDict):
    def __init__(self,data={},**kwargs):
        UserDict.__init__(self)
        self.update(data)
        self.update(kwargs)

    def __add__(self, other):
        dict = FancyDict(self.data)
        dict.update(other)
        return dict

a = FancyDict(a=1)
b = FancyDict(b=1)
print a+b
