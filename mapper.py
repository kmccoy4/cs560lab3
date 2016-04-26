#mapper

import sys, re

totalsubs = 0
subjects = {}

if 

for i,line in enumerate(sys.stdin):
    if i is 0:
        totalsubs = line
        print totalsubs
    elif line.find("Subject: ") >= 0:

