#mapper

import sys, re


totalsubs = 0
subjects = {}
rank = {}
nodes = {}
sub = ""
#getinfo
for line in sys.stdin:
    if line.find("Subject: ") >= 0:
        sub = line[9:len(line)]
        sub = sub.strip('\n')
        subjects[sub] = []
    else:
        line = line.strip('\n')
        try:
            nodes[line].append(sub)
        except:
            nodes[line] = []
            nodes[line].append(sub)
        rank[line] = float(sys.stdin.next())

for s in nodes:
    print s
    print nodes[s]

#pagerank
#for sub in subjects:
#    print sub
#    for l in subjects[sub]:
#        print "%s,%.20f" % (l,float(rank[sub])/len(subjects[sub]))
        
