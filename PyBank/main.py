# Calculate the total number of months 
import os
import csv

# create path to csv file to read data
budget_data = os.path.join("Resources", "budget_data.csv")

# text file to hold the output of the revenue analysis
outputFile = os.path.join("revenueAnalysis.text")

#variables:
total_Months = 0 # initialize the total to 0
total_Revenue= 0  # initialize the total to 0
monthly_Changes = [] # initialize list of monthly net changes
months= []          # initializes the list of months

# read the csv file
with open(budget_data) as budget_data:
    #create a scv reader object
    csvreader= csv.reader(budget_data)

    #read the header row
    header = next(csvreader)
    # move the first row
    first_Row= next(csvreader)

    #increment the count of the total months
    total_Months += 1 # same as totalMonths +1 

    # add on to the amount of revenue
            #revenue is in index 1
    total_Revenue += float(first_Row[1]) # have to convert variables to readable numbers
    
    #establish the previous revenues
        #revenue is in index 1
    previous_Revenue = float(first_Row[1])

    #break out the rest of the csv file into rows. 
    #so for every row in our csv reader, we are going to increment 
    # the count of the total months, and have it skip the first row (because it contains column names)
    for row in csvreader:
        #increment the count of the total months
        total_Months += 1 # same as totalMonths +1 

        # add on to the amount of revenue
            #revenue is in index 1
        total_Revenue += float(row[1]) # have to convert variables to readable numbers
        
        # calculate the net change
        net_Change= float(row[1]) - previous_Revenue
        # add to the list of monthly changes
        monthly_Changes.append(net_Change)

        # add the first month that a change occurred
            # month is in index 0
        months.append(row[0])

        #update the previous revenue
        previous_Revenue = float(row[1])

# Calculate the average net change per month 
average_Change_Per_month = sum(monthly_Changes) / len(monthly_Changes)

greatest_Increase = [months[0], monthly_Changes[0]] # holds the month and the value of the greatest increase
greatest_Decrease = [months[0], monthly_Changes[0]] # holds the month of and the value of th greatest decrease

#use this loop to calculate the index of the greatest and least monthly change
for m in range(len(monthly_Changes)):
    # calculate the greatest increase and decrease
    if(monthly_Changes[m]> greatest_Increase[1]):
        # if the value is greater than the greatest increase, that value becomes the new greatest increase
        greatest_Increase[1]= monthly_Changes[m]
        # update the month
        greatest_Increase[0] = months[m]

    if(monthly_Changes[m]< greatest_Decrease[1]):
        # if the value is less than the greatest decrease, that value becomes the new greatest decrease
        greatest_Decrease[1]= monthly_Changes[m]
        # update the month
        greatest_Decrease[0] = months[m]

# start generating the output for the text file. Call the variable "output". \n = new line, \t = tab
output= (
    f"Financial Analysis \n"
    f"------------------------ \n"
    f"\t Total Months - {total_Months} \n"
    f"\t Total Revenue - ${total_Revenue:,.2f}\n" # separate with commas and have 2 decimal points
    f"\t Average Change per Month - ${average_Change_Per_month:,.2f}\n"
    f"\t Greatest Increase - {greatest_Increase[0]} Amount $ {greatest_Increase[1]:,.2f}\n"
    f"\t Greatest Decrease - {greatest_Decrease[0]} Amount $ {greatest_Decrease[1]:,.2f}\n"
)

# print the output to the terminal 
print(output)

#export the output variable to the text file
with open(outputFile, "w") as textfile:
    textfile.write(output)