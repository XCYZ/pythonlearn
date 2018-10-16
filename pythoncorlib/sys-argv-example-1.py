import sys
args = sys.argv
length = len(args)
print "script name is", args[0]
if length>1:
    for arg in args[1:length]:
        print arg
else:
    print "no arg"
