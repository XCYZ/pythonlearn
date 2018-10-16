import mmap
import os

filename = "sctringio-example-1.py"

file = open(filename,"r+")
size = os.path.getsize(filename)

data = mmap.mmap(file.fileno(),size)
print data
print len(data),size