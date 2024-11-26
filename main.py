import csv

f = open('data.csv', mode='r', newline='')
# Load the CSV data
reader = csv.DictReader(f)

WIKITEXT = """{{{{Clothing infobox
|uid={}
|display={}
|craft slots={}
}}}}"""

CRAFT_SLOT_TEXT = """{{{{CraftSlot|id={} |amount={} }}}}"""

# Example of reusing the reader
for row in reader:
    craft_slots = []
    for i in range(5):  # 0, 1, 2, 3, 4
        j = str(i + 1)  # 1, 2, 3, 4, 5
        idname = 'Craft Slot ' + j + ' ID'  # Craft Slot 1 ID
        amountname = 'Craft Slot ' + j + ' Amount'  # Craft Slot 1 Amount
        if row[idname] != '':
            craft_slots.append(  # lua: craft_slots[#craft_slots+1] =
                CRAFT_SLOT_TEXT.format(row[idname], row[amountname])
            )

    print(WIKITEXT.format(
        row['UID'],
        row['-Friendly Name-'],
        ''.join(craft_slots)
    ))

# cleanup
f.close()
