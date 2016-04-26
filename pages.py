#script to parse the page titles from Simple English Wikipedia

import sys, re, string

def xmlreplace(s):
    s = s.replace("&quot;","")
    s = s.replace("&lt;","<")
    s = s.replace("&gt;",">")
    s = s.replace("&apos;"," ")
    s = s.replace("&amp;","&")
    s = s.replace("\'","_")
    s = s.replace(" ","_")
    return s

re.compile('[a-zA-Z0-9]')

#get all titles
if len(sys.argv) < 2:
    print("usage: pages.py <titles_file>")
    sys.exit(1)
    
f = open(sys.argv[1],"r")
titles = f.read().splitlines()
f.close()

subjects = {}
for title in titles:
    title = title.lower()
    title = xmlreplace(title)
    if title not in subjects:
        subjects[title] = []

pages = {}
for line in sys.stdin:
        line = line.lower()
        pos = line.find('<title>')
        if pos >= 0 and line.find(":") < 0:
            #print "%s%s" % ("Subject: ",line[pos+7:len(line)-9]);
            #add to dictionary
            subject = line[pos+7:len(line)-9]
            subject = xmlreplace(subject)
            if subject not in subjects:
                continue
            pages[subject]=[]
            #find associated text links
            line = sys.stdin.next();
            #skip lines not in text tags
            while(line.find('<text') < 0):
                line = sys.stdin.next();

            while(line.find('</text>') < 0):
                line = line.lower()
                line = xmlreplace(line)
                links = re.findall(r"(?<!'')\[\[[\w|\||\s|-|&|,|\.|!|\?|\(|\)|%|#|\*|;|\+|-|=|_|\^|\$|@|~]*\]\]",line)

                for l in links:
                        if l.find("|") < 0:
                            l = l[2:len(l)-2]
                        elif l.find("#") > 0:
                            l = l[2:l.find("#")]
                        else:
                            l = l[2:l.find("|")]
                        if l in subjects:
                            pages[subject].append(l)
                line = sys.stdin.next();

#print pages
#remove links that do not exist as a subject (excess links, links that were not marked red)
#for sub in pages:
    #print "Subject: %s" % sub
    #print pages[sub]
#    for l in pages[sub]:
#        if l not in pages:
            #print "removing %s" % l
#            pages[sub].remove(l)

#print dictionary
for sub in pages:
    print "Subject: %s" % sub
    print pages[sub]
#    for l in pages[sub]:
#        print l
