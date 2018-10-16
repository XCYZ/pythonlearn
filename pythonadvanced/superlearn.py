class A(object):
    abc = "abc"

    def get_abc(self):
        return self.abc


class B(object):
    abc = 1


class C(A, B):
    xyz = "xyz"
