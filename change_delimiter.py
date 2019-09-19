import csv
import sys
import os

directory = "/home/cypher/Desktop/IDIF/"

inputPath = sys.argv[1]
outputPath = os.path.dirname(inputPath) + "/output.csv"

# https://stackoverflow.com/a/27553098/3357935
print("Converting CSV to tab-delimited file...")
with open(inputPath) as inputFile:
	with open(outputPath, 'w', newline='') as outputFile:
		reader = csv.DictReader(inputFile, delimiter=',')
		writer = csv.DictWriter(outputFile, reader.fieldnames, delimiter='|')
		writer.writeheader()
		writer.writerows(reader)
print("Conversion complete.")