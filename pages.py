#script to parse the page titles from Simple English Wikipedia

import sys, re

def main():
    regex = re.compile('[^a-zA-Z]')
    for line in sys.stdin:
        if line.find("<title>") > 0:
            print '%s' % (line);


if __name__ == "__main__":
    main()
