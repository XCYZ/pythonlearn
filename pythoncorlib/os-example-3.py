import os
import string


def replace(file, search_for, replace_with):
    back = os.path.splitext(file)[0]+".bak"
    tmp = os.path.splitext(file)[0]+".tmp"
    try:
        os.remove(tmp)
    except OSError:
        pass
    fi = open(file)
    fo = open(tmp)
    for line in fi.readlines():
        fo.write(string.replace(line, search_for, replace_with))
    fi.close()
    fo.close()
