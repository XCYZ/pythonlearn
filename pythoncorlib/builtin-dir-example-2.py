class A:
    def a(self):
        pass

    def b(self):
        pass


class B(A):
    def c(self):
        pass

    def d(self):
        pass


def get_members(clazz,mebers=None):
    if mebers is None:
        mebers = []
    for k in clazz.__bases__:
        get_members(k, mebers)
    for m in dir(clazz):
        if m not in mebers:
            mebers.append(m)
    return mebers


print get_members(A)
print get_members(B)
print get_members(IOError)