class Fab(object):

    def __init__(self, max):
        self.max = max
        self.n = 0
        self.a = 1
        self.b = 0

    def __iter__(self):
        while self.n < self.max:
            yield self.a
            self.a, self.b = self.a + self.b, self.a
            self.n = self.n + 1


if __name__ == "__main__":
    f = Fab(10)
    for x in f:
        print(x)

