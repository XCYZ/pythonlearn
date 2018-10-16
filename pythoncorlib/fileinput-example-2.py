import fileinput
import glob
import string,sys

for line in fileinput.input(glob.glob("*.py")):
    if fileinput.isfirstline():
        sys.stderr.write("-----reading%s--\n"%fileinput.filename())
    sys.stdout.write(str(fileinput.lineno())+" "+string.upper(line))
