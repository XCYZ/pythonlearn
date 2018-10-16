import re
text = "The Attila the Hun Show"
m = re.match(".",text)
if m:print repr("."),"=>",repr(m.group(0))
m = re.match(".*", text)
if m:print repr("all"),"=>",repr(m.group(0))
m = re.match("\w+",text)
if m:print repr("word"),"=>",repr(m.group(0))