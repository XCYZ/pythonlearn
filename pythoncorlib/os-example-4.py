import os
cwd = os.getcwd()
print cwd
os.chdir("..")
cwd = os.getcwd()
print cwd