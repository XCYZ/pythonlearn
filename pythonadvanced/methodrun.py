import abc


class Pazz(object):

    @staticmethod
    def get_name():
        return "sb"

    @classmethod
    def create_instance(cls, size):
        return cls(size)

    @staticmethod
    def get_redias():
        raise NotImplemented

    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def __eq__(self, other):
        return self.size == other.size


class BasePazz(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_redias(self):
        """method not implemented"""




