from cStringIO import StringIO

MESSAGE = "I Love Qi Jie"
file = StringIO(MESSAGE)
print file.read()