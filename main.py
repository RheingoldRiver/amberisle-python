import csv

f = open('data.csv', mode='r', newline='')
# Load the CSV data
reader = csv.DictReader(f)

WIKITEXT = """{{{{Clothing infobox
|uid={}
|display={}
|craft slots={}
}}}}"""

# Example of reusing the reader
for row in reader:

    craft_slot_value1 = '{{CraftSlot|' + row['Craft Slot 1 ID'] + '|' + row['Craft Slot 1 Amount'] + '}}'
    craft_slot_value2 = '{{CraftSlot|' + row['Craft Slot 2 ID'] + '|' + row['Craft Slot 2 Amount'] + '}}'
    craft_slot_value3 = '{{CraftSlot|' + row['Craft Slot 3 ID'] + '|' + row['Craft Slot 3 Amount'] + '}}'

    print(WIKITEXT.format(
        row['UID'],
        row['-Friendly Name-'],
        craft_slot_value1 + '\n' + craft_slot_value2 + '\n' + craft_slot_value3
    ))

# cleanup
f.close()
