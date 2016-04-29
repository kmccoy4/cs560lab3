To access the latest Simple English Wikipedia dump:
https://dumps.wikimedia.org/simplewiki/latest/

Preprocessing:

python pages.py \<wiki_titles_file\> < simplewikifile.xml > output.txt

Mapper (run once):

python mapper.py < output.txt > mapper1.txt

Reducer (run iteratively):

python reducer.py < mapper1.txt > reducer1.txt

python reducer.py < reducer2.txt > reducer2.txt

etc.

Reducer output files display:

Subject: example

outlink1

PR(outlink1)

outlink2

PR(outlink2)

etc.

