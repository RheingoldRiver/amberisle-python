* [Video lesson](https://www.youtube.com/watch?v=L15HH3P4r7Y)
* [Amber Isle wiki](https://amberisle.wiki.gg)
* [Additional example Python repo](https://github.com/RheingoldRiver/sorcerer-update) (this one contains an update script in addition to a page creation script)

Boilerplate code used in the class:

```python
import csv

f = open('data.csv', mode='r', newline='')
# Load the CSV data
reader = csv.DictReader(f)

# Example of reusing the reader
for row in reader:
    print(row)

# cleanup
f.close()
```
