class LazyImport(object):
    def __init__(self,module_name):
        self.module_name = module_name
        self.module = None

    def __getattr__(self, item):
        if self.module is None:
            self.module = __import__(self.module_name)
        return getattr(self.module, item)


string = LazyImport("string")
print string.lowercase
