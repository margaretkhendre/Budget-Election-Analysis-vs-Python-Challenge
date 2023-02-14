import os 
import csv
# create path to csv file
election_data_csv = os.path.join("Resources", "election_data.csv")

print("Election Results")

with open(election_data_csv) as csvFile:

    csvReader = csv.reader(csvFile, delimiter=',')
# skip the first row, and establish your count to start at 0
    rowindex= 0
    couter = 0
    header = next(csvReader)

    for row in csvReader:
        # print the first column to make sure you're working with the proper bit of data
        print(row[0])
        # calculate the total using sum function and print 
        total = sum(int(row[0]))
        print(total)
print(total)
print("winner:")
