import csv

f = open('data.csv', mode='r', newline='')
# Load the CSV data
reader = csv.DictReader(f)

WIKITEXT = """{{{{Clothing infobox
|uid={}
|display={}
}}}}"""

# Example of reusing the reader
for row in reader:
    print(WIKITEXT.format(
        row['UID'],
        row['-Friendly Name-']
    ))

# cleanup
f.close()
