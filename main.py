import csv

f = open('data.csv', mode='r', newline='')
# Load the CSV data
reader = csv.DictReader(f)

# Example of reusing the reader
for row in reader:
    print(row)

# cleanup
f.close()
