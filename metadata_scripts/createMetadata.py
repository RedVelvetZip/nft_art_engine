# importing csv module
import csv
import glob
import os

# csv file name
filename = "json raw3.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
	# creating a csv reader object
	csvreader = csv.reader(csvfile)
	
	# extracting field names through first row
	fields = next(csvreader)

	# extracting each data row one by one
	for row in csvreader:
		rows.append(row)

	# get total number of rows
	print("Total no. of rows: %d"%(csvreader.line_num))

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

# printing data in JSON files in metadata folder
os.chdir("./metadata")
print('\nNow writing JSON files...\n')
f_total = open("_metadata.json", "w+")
f_total.write('[\n')
for row in rows[:2222]:
    f = open((row[0]) + ".json", "w+")
    #write to the individual json file
    f.write('{\n')
    f.write('    "name": "? '+row[0]+'",\n')
    f.write('    "description": "???",\n')
    f.write('    "image": "'+row[4]+'",\n')
    # f.write('    "animation_url": "'+row[3]+'",\n')
    f.write('    "attributes": [\n')
    f.write('      {\n')
    f.write('        "trait_type": "Background",\n')
    f.write('        "value": "'+row[6]+'"\n')
    f.write('      },\n')
    f.write('      {\n')
    f.write('        "trait_type": "Innovation",\n')
    f.write('        "value": "'+row[6]+'"\n')
    f.write('      },\n')
    f.write('      {\n')
    f.write('        "trait_type": "Compatibility",\n')
    f.write('        "value": "'+row[7]+'"\n')
    f.write('      },\n')
    f.write('      {\n')
    f.write('        "trait_type": "Variation",\n')
    f.write('        "value": "'+row[8]+'"\n')
    f.write('      }\n')
    f.write('    ]\n')
    f.write('  }\n')
    f.close()
    #write to the total json file
    f_total.write('  {\n')
    f_total.write('      "name": "? '+row[0]+'",\n')
    f_total.write('      "description": "???",\n')
    f_total.write('      "image": "'+row[4]+'",\n')
    # f_total.write('      "animation_url": "'+row[3]+'",\n')
    f_total.write('      "attributes": [\n')
    f_total.write('        {\n')
    f_total.write('          "trait_type": "Compound",\n')
    f_total.write('          "value": "'+row[5]+'"\n')
    f_total.write('        },\n')
    f_total.write('        {\n')
    f_total.write('          "trait_type": "Innovation",\n')
    f_total.write('          "value": "'+row[6]+'"\n')
    f_total.write('        },\n')
    f_total.write('        {\n')
    f_total.write('          "trait_type": "Compatibility",\n')
    f_total.write('          "value": "'+row[7]+'"\n')
    f_total.write('        },\n')
    f_total.write('        {\n')
    f_total.write('          "trait_type": "Variation",\n')
    f_total.write('          "value": "'+row[8]+'"\n')
    f_total.write('        }\n')
    f_total.write('      ]\n')
    f_total.write('    },\n')
f_total.write(']\n')
f_total.close()