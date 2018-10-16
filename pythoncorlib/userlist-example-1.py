from UserList import UserList


class AutoList(UserList):
    def __setitem__(self, key, value):
        if key == len(self.data):
            self.data.append(value)
        else:
            self.data[key] = value

