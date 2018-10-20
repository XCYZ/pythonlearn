import time
from functools import wraps


def cal_time(f):
    @wraps(f)
    def wrap_f(*args,**kwargs):
        start = time.time()
        f(*args,**kwargs)
        end = time.time()
        print(end-start)
    return wrap_f


def cache(f):
    _cache = {}

    @wraps(f)
    def wrap_f(*args):
        result = _cache.get(args)
        if result:
            return result
        else:
            result = f(*args)
            _cache[args] = result
            return result
    return wrap_f


def fab1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fab1(n-1)+fab1(n-2)


@cache
def fab2(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fab2(n-1)+fab2(n-2)


if __name__ == "__main__":
    t1 = time.time()
    fab1(40)
    t2 = time.time()
    fab2(50)
    t3 = time.time()
    print(t2-t1)
    print(t3-t2)
