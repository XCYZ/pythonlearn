import os


def index(directory):
    stack = [directory]

    while stack:
        directory = stack.pop()
        for file in os.listdir(directory):
            fullname = os.path.join(directory, file)
            yield fullname
            if os.path.isdir(fullname) and not os.path.islink(fullname):
                stack.append(fullname)


for file in index(".."):
    print file

print len(list(index("..")))