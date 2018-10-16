from functools import wraps


def wai(f):
    @wraps(f)
    def nei(*args,**keyargs):
        print("call")
        f(*args, **keyargs)
        print("ending")
    return nei


@wai
def test():
    """test"""
    print("test")