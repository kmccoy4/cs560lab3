#mapper

import sys, re

totalsubs = 0
subjects = {}
rank = {}
#getinfo
for i,line in enumerate(sys.stdin):
    if i is 0:
        totalsubs = line
    elif line.find("Subject: ") >= 0:
        sub = line[9:len(line)]
        sub = sub.strip('\n')
        subjects[sub] = []
        #get links on next line
        line = sys.stdin.next()
        rank[sub] = float(line)
        line = sys.stdin.next()
        links = re.findall(r"\'[\w|\||\s|-|&|,|\.|!|\?|\(|\)|%|#|\*|;|\+|-|=|_|\^|\$|@|~]*\'",line)
        for l in links:
            l = l.strip('\'')
            l = l.strip('\n')
            subjects[sub].append(l)
#initial pagerank
for sub in subjects:
    print "Subject: %s" % sub
    for l in subjects[sub]:
        #print "%s\n%.30f" % (l,float(rank[sub])/len(subjects[sub]))
        print "%s\n%.30f" % (l,float(rank[sub]))
