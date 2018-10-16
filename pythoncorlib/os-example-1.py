import os
import time


def dump(file):
    mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = os.stat(file)
    print "- size:", size, "bytes"
    print "- owner:", uid, gid
    print "- created:", time.ctime(ctime)
    print "- last accessed:", time.ctime(atime)
    print "- last modified:", time.ctime(mtime)
    print "- mode:", oct(mode)
    print "- inode/dev:", ino, dev


dump("hello.py")