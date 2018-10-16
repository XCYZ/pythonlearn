def dump(fun):
    if callable(fun):
        print fun,"is callable"
    else:
        print fun,"is not callable"


class A:
    def method(self, value):
        return value


class B(A):
    def __call__(self, value):
        return value

a = A()
b = B()

dump(a)
dump(b)
dump(A)
dump(B)