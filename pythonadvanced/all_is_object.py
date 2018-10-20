def ask(name=None):
    print(name)

class Person():
    def __init__(self):
        print("aaaaaaaa")

my_func = ask
P = Person
def f1():
    return ask
list1 = []
list1.append(my_func)
list1.append(P)

for f in list1:
    f()

p = P()

my_func("zhsan")
f1()("name")