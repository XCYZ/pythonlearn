import re
text = "you're no fun anymore..."

print re.sub("fun","integering",text)

print re.sub("[^\w]","-",text)