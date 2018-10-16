import tempfile
import os

temp = tempfile.mktemp()
print "tempfile","=>",temp

file = open(temp,"w+b")
file.write("*"*100)
file.seek(0)
print len(file.read()),"bytes"
file.close()