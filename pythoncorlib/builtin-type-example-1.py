def load(file):
    if isinstance(file,type("")):
        file = open(file,"rb")
    return file.read()


print len(load("builtin-dir-example-1.py")),"bytes"
print len(load(open("builtin-dir-example-1.py","rb"))),"bytes"
