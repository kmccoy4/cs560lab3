#script to parse the page titles from Simple English Wikipedia

import sys, re, string

re.compile('[a-zA-Z_0-9]')
pages = {}
for line in sys.stdin:
    pos = line.find("<title>")
    if pos >= 0 and line.find(":") < 0:
        #print "%s%s" % ("Subject: ",line[pos+7:len(line)-9]);
        #add to dictionary
        subject = line[pos+7:len(line)-9]
        pages[subject]=[]
        #find associated text links
        line = sys.stdin.next();
        #skip lines not in text tags
        while(line.find("<text") < 0):
            line = sys.stdin.next();

        while(line.find("</text>") < 0):
            links = re.findall(r"\[\[[\w|\|\s]*\]\]",line)
            for l in links:
                if l.find("|") < 0:
                    #print "%s\t%d" % (l[2:len(l)-2],1)
                    pages[subject].append(l[2:len(l)-2])
                else:
                    #print "%s\t%d" % (l[2:l.find("|")],1)
                    pages[subject].append(l[2:l.find("|")])
            line = sys.stdin.next();

#print dictionary
for sub in pages:
    print "Subject: %s" % sub
    for l in pages[sub]:
        print l
