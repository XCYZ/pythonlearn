import sys
print "path has", len(sys.path), "members"
sys.path.append("..")
print "path has", len(sys.path), "members"
sys.path = []
import random