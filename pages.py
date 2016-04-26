#script to parse the page titles from Simple English Wikipedia

import sys, re, string

def xmlreplace(s):
    s = s.replace("&quot;","")
    s = s.replace("&lt;","<")
    s = s.replace("&gt;",">")
    s = s.replace("&apos;","\'")
    s = s.replace("&amp;","&")        
    return s

re.compile('[a-zA-Z0-9]')

pages = {}
for line in sys.stdin:
        line = line.lower()
        pos = line.find('<title>')
        if pos >= 0 and line.find(":") < 0:
            #print "%s%s" % ("Subject: ",line[pos+7:len(line)-9]);
            #add to dictionary
            subject = line[pos+7:len(line)-9]
            subject = xmlreplace(subject)
            pages[subject]=[]
            #find associated text links
            line = sys.stdin.next();
            #skip lines not in text tags
            while(line.find('<text') < 0):
                line = sys.stdin.next();

            while(line.find('</text>') < 0):
                line = line.lower()
                line = xmlreplace(line)
                links = re.findall(r"(?<!'')\[\[[\w|\||\s|-|&|,|\.|!|\?|\(|\)|%|#|\*|;|\+|-|=|_|\^|\$|@|~|\']*\]\]",line)
                for l in links:
                        if l.find("|") < 0:
                            #print "%s\t%d" % (l[2:len(l)-2],1)
                            pages[subject].append(l[2:len(l)-2])
                        elif l.find("#") > 0:
                            pages[subject].append(l[2:l.find("#")])
                        else:
                            #print "%s\t%d" % (l[2:l.find("|")],1)
                            pages[subject].append(l[2:l.find("|")])
                line = sys.stdin.next();

#print pages
#remove links that do not exist as a subject (excess links, links that were not marked red)
for sub in pages:
    #print "Subject: %s" % sub
    #print pages[sub]
    for l in pages[sub]:
        if l not in pages:
            #print "removing %s" % l
            pages[sub].remove(l)

#print dictionary
#for sub in pages:
    print "Subject: %s" % sub
    print pages[sub]
#    for l in pages[sub]:
#        print l
