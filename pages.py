#script to parse the page titles from Simple English Wikipedia

import sys, re

def main():
    for line in sys.stdin:
        pos = line.find("<title>")
        if pos >= 0 and line.find(":") < 0:
            print '%s' % (line[pos+7:len(line)-9]);


if __name__ == "__main__":
    main()
