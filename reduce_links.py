import sys
from operator import itemgetter

def main(separator='\t'):
    current_link = None
    current_count = 0
    link = None

    for line in sys.stdin:
        if line.find("Subject:"):
            continue

        line = line.strip()

        link, count = line.split("\t")

        try:
            count = int(count)
        except ValueError:
            continue

        if current_link == link:
            current_count += count
        else:
            if current_link:
                print "%s\t%s" % (current_link, current_count)
            current_count = count
            current_link = link

    if current_link == link:
        print "%s\t%s" % (current_link, current_count)

if __name__ == "__main__":
    main()
