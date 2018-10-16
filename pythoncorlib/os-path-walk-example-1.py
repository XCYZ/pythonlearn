import os


def callback(arg, dir, files):
    for file in files:
        print os.path.join(dir, file), repr(arg)


os.path.walk(".",callback,"sb")
