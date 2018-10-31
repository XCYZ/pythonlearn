class User:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,name):
        self.name = name


if __name__ == "__main__":
    u = User('Alex')
