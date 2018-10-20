import logging
from time import time,localtime,strftime,sleep
from random import choice


class CallingInfo(object):
    def __init__(self,name):
        log = logging.getLogger(name=name)
        log.setLevel(logging.INFO)
        handler = logging.FileHandler(name+".log")
        log.addHandler(handler)
        log.info("==========start=======")
        self.log = log
        self.formatter = '%(func)s -> [%(time)s - %(used)s - %(calls)s]'

    def info_log(self, fun):
        def wrap_func(*args, **kwargs):
            wrap_func.call_time += 1
            lt = localtime()
            start = time()
            res = fun(*args,**kwargs)
            used = start - time()
            info = {
                'func':fun.__name__,
                'time':strftime("%x",lt),
                'used':used,
                'calls':wrap_func.call_time

            }
            message = self.formatter % info
            self.log.info(message)
            return res
        wrap_func.call_time = 0
        return wrap_func

    def close_log(self):
        self.log.setLevel(logging.ERROR)

    def set_formatter(self,formatter):
        self.formatter = formatter


log1 = CallingInfo('log01')
log2 = CallingInfo('log02')


@log1.info_log
def f():
    print('f')
    sleep(choice([0,1,2]))


@log1.info_log
def g():
    print('g')
    sleep(choice([0, 1, 2]))


@log2.info_log
def h():
    print('h')
    sleep(choice([0, 1, 2]))


if __name__ == "__main__":
    for x in range(50):
        choice([f, g, h])()
