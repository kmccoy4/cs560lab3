#script to parse the page titles from Simple English Wikipedia

import sys, re, string

def main():
    for line in sys.stdin:
        pos = line.find("<title>")
        if pos >= 0 and line.find(":") < 0:
            print '%s%s' % ("Subject: ",line[pos+7:len(line)-9]);
            #find associated text links
            line = sys.stdin.next();
            #skip lines not in text tags
            while(line.find("<text") < 0):
                line = sys.stdin.next();

            while(line.find("</text>") < 0):
                #nline = line.replace('|','; ')
                #nline = nline.replace(' ',';')
                #words = re.split(r'[ |]',line)
                words = line.split()
                num = 0
                for index,word in enumerate(words):
                    wpos = word.find("[[")
                    if wpos >= 0 and word.find(":") < 0 and word.find(".jpg") < 0:
                        catstr = ""
                        endpos = word.find("]]")
                        if endpos > 0:
                            if word.find("|") > 0:
                                print '%s%s%s%d'% ('\t', word[wpos+2:word.find("|")],'\t',1)
                            else:
                                print '%s%s%s%d'% ('\t', word[wpos+2:endpos],'\t',1)
                        else:
                            catstr += word
                            catstr += " "
                        if endpos < 0:
                            #get next word
                            tempword = ""
                            num = 1
                            if index+1 < len(words):
                                tempword = words[index+1]
                            while(tempword.find("]]") < 0):
                                catstr += tempword
                                catstr += " "
                                num+=1
                                if index+num >= len(words):
                                    break
                                tempword = words[index+num]
                            catstr += tempword
                            if catstr.find("|") > 0:
                                catstr = catstr[:catstr.find("|")]
                                catstr += "]]"
                            print '%s%s%s%d' % ('\t',catstr[catstr.find("[[")+2:catstr.find("]]")],'\t',1);
                        #endpos = word.find("]]")
#print '%s%s' % ('\t',word[wpos+2:endpos]);
                line = sys.stdin.next();
                

if __name__ == "__main__":
    main()
