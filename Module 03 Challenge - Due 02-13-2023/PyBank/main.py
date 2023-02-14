# Calculate the total number of months 
import os
import csv
    # create path to csv file
budget_data_csv = os.path.join("Resources", "budget_data.csv")

print("Financial Analysis")

with open(budget_data_csv) as csvFile:
    
    csvReader = csv.reader(csvFile,delimiter= ',')
    # skip the first row, and establish your count to start at 0
    rowindex = 0
    counter = 0 
    header = next(csvReader)
 
    for row in csvReader:  
        # create a counter to calculate the total number of months and print it 
        counter = counter + 1
print(" Total Months:", + counter)

# Calculate the net total amount of "Profit/Losses" over the entire period 
with open(budget_data_csv) as csvFile:
    csvReader= csv.reader(csvFile, delimiter= ',')
    
    total = 0
    # skip the first row 
    header = next(csvReader)

    for row in csvReader:
        # calculate the total using the sum function and print it 
        profitLossesTotal = sum(int(row[1]))
       
print(" Total:", profitLossesTotal)
        
# Calculate the changes in "Profit/Losses" over the entire period, and then the average of those changes
avg = sum(row[1])/ len(row[1])
print("Total Average:", + avg)