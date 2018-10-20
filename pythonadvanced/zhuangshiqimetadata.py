from functools import wraps
import inspect


def type_assert(*type_args,**type_kwargs):
    def decorator(func):
        func_sig = inspect.signature(func)
        bind_type = func_sig.bind_partial(*type_args,**type_kwargs).arguments

        @wraps(func)
        def real_func(*args,**kwargs):
            arguments = func_sig.bind_partial(*args, **kwargs).arguments
            for name,obj in arguments.items():
                type_ = bind_type.get(name)
                if type_:
                    if not isinstance(obj, type_):
                        raise TypeError('%s must be %s instance' % (obj,type_))
            return func(*args,**kwargs)
        return real_func
    return decorator


if __name__ == "__main__":
    @type_assert(int,int,str)
    def f1(a,b,c):
        return a,b,c
    f1("a","v","u")

