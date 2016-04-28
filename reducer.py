#reducer

import sys, re


subjects = {}
rank = {}
newrank = {}
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
        subjects[sub].append(line)

for subj in nodes:
    tmp = 0.0
    for n in nodes[subj]:
        try:
            tmp += rank[n]/len(subjects[n])
        except:
            rank[n] = 0.0
            tmp += 0.0
    #calculate and add new rank
    tmp = (tmp * 0.85) + ((1-0.85)/len(subjects))
    newrank[subj] = tmp
    #print subj
    #print newrank[subj]

#pagerank
for s in subjects:
    print "Subject: %s" % s
    for l in subjects[s]:
        print "%s\n%.30f" % (l,float(newrank[l]))
        
