import sys
import csv
geneSymbol = sys.argv[1] 

filename = "results.csv"
data = [geneSymbol,'testCode']
with open(filename, 'w+', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

        # Write data to the CSV file row by row
    for row in data:
        csvwriter.writerow([row])
