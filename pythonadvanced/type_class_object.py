a = 1
b = "abc"
print(type(1))
print(type(int))

print(type(b))
print(type(str))


class Student:
    pass


class MyStudent(Student):
    pass


stu = Student()
print(type(stu))
print(type(Student))
print(int.__bases__)
print(str.__bases__)
print(type.__bases__)
print(type(object))
print(object.__bases__)
print(type(type))