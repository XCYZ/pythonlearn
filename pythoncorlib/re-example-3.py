import re
text = "Example 3: There is 1 date 10/25/95 in here!"
m = re.search("(\d{1,2})/(\d{1,2})/(\d{1,2})",text)
if m:
    print m.group(0)
    print m.group(1,2,3)