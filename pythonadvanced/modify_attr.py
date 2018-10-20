from functools import wraps
import time
import logging
import random


def warn_timeout(timeout):
    def decorator(func):
        @wraps(func)
        def wrap_func(*args, **kwargs):
            start = time.time()
            res = func(*args,**kwargs)
            used = time.time() - start
            if used > timeout:
                logging.warning("%s: %s>%s" % (func.__name__,used,timeout))
            return res

        def set_timeout(new_timeout):
            nonlocal timeout
            timeout = new_timeout
        wrap_func.set_timeout = set_timeout
        return wrap_func
    return decorator


if __name__ == "__main__":
    @warn_timeout(timeout=1.5)
    def f(i):
        print('in f [%s]' % i)
        while random.randint(0,1):
            time.sleep(1)


    f.set_timeout(1)

    for i in range(30):
        f(i)
