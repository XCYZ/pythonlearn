def fun(a, b):
    print a, b


if __name__ == "__main__":
    apply(fun,("a","b"))
    apply(fun,(1,2))