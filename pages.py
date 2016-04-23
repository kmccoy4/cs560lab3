#script to parse the page titles from Simple English Wikipedia

import sys, re, string

def main():
    re.compile('[a-zA-Z_0-9]')
    for line in sys.stdin:
        pos = line.find("<title>")
        if pos >= 0 and line.find(":") < 0:
            print "%s%s\t1" % ("Subject: ",line[pos+7:len(line)-9]);
            #find associated text links
            line = sys.stdin.next();
            #skip lines not in text tags
            while(line.find("<text") < 0):
                line = sys.stdin.next();

            while(line.find("</text>") < 0):
                links = re.findall(r"\[\[[\w|\|\s]*\]\]",line)
                for l in links:
                    if l.find("|") < 0:
                        print "%s\t%d" % (l[2:len(l)-2],1)
                    else:
                        print "%s\t%d" % (l[2:l.find("|")],1)
                line = sys.stdin.next();



if __name__ == "__main__":
    main()
