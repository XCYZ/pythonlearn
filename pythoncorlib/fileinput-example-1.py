import fileinput
import sys

for line in fileinput.input("os-example-3.py"):
    sys.stdout.write("->")
    sys.stdout.write(line)