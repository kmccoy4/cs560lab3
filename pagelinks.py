import sys
import re

if len(sys.argv) < 3:
	print("usage:pagelinks.py <titles_file> <pages_file>")
	sys.exit(1)

f = open(sys.argv[1],"r")
titles = f.read().splitlines()
f.close()

subjects = {}
for title in titles:
	title = title.lower()
	if title not in subjects:
		subjects[title] = []

f = open(sys.argv[2],"r")
lines = f.read().splitlines()
f.close()

count = 0
readingPage = False
pages = {}
for line in lines:
	if "<page>" in line and not readingPage:
		readingPage = True
		pages[count] = []
	elif "</page>" in line and readingPage:
		readingPage = False
		count += 1
	elif readingPage:
		pages[count].append(line)	

textRegex = re.compile('<text.*?>(.*?)</text>')
linkRegex = re.compile('\[\[(.*?)\]\]')
for page in pages:
	pageContents = pages[page]
	for line in pageContents:
		if "<title>" in line:
			start = line.index("<title>") + len("<title>")
			end = line.index("</title>",start)
			subject = line[start:end]
			subject = subject.lower()
			subject = subject.replace(" ","_")
			if subject in subjects:
				content = " ".join(pageContents)
				text = textRegex.search(content)
				if text:
					t = text.group(0)
					links = linkRegex.findall(t)
					if links:
						for link in links:
							link = link.lower()
							link = link.replace(" ","_")
							if link in subjects:
								subjects[subject].append(link)	


search = raw_input("Enter search term to begin (or ENTER to exit): ")
if search in subjects:
	print("search results for '" + search + "':")
	for entry in subjects[search]:
		print(entry)
elif len(search) > 0:
	print("no results found for '" + search + "'")

while search:
	search = raw_input("Enter search term to begin (or ENTER to exit): ")
	if search in subjects:
		print("search results for '" + search + "':")
		for entry in subjects[search]:
			print(entry)
	elif len(search) > 0:
		print("no results found for '" + search + "'")
