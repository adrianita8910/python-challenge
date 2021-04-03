import os
import csv

# Define variables
months = []
valueChanges = []
countMonths = 0
netValue = 0
previosMonthValue = 0
valueChange = 0

#Path to collect the data
budget_csv = os.path.join("..", "Resources", "budget_data.csv")

#Specify an output folder
output_path = os.path.join("Financial_Analysis.txt")

#Open and read the csv file
with open(budget_csv, newline="") as csvFile:

    # Split the data with delimiters
    csvreader = csv.reader(csvFile, delimiter=",")

    #Skip the header row
    csv_header = next(csvFile)
    #print(f"Header:{csv_header}")

    

    #Read through each row of data skipping the header row
    for row in csvreader:

        #The total number of months included in the dataset
        countMonths += 1

        #The net total amount of "Profit/Losses" over the entire period
        currentMonthvalue = int(row[1])
        netValue += currentMonthvalue

        if(countMonths == 1):
            #Define the value of previos month is equal to current month
            previosMonthValue = currentMonthvalue
            continue

        else:

            #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
            valueChange = currentMonthvalue - previosMonthValue

            #Append 
            months.append(row[0])
            valueChanges.append(valueChange)

            #Make the current month loss to be previos month profit loss for the next loop 
            previosMonthValue = currentMonthvalue

        #Sum and average of the changes in "Profit/Losses" over the entire period
        sumValue = sum(valueChanges)
        meanValue = round(sumValue/(countMonths - 1), 2)

        #Highest and lowest change in "profit/Losses" over the entire period
        highestChange = max(valueChanges)
        lowestChange = min(valueChanges)

         #Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
        highestMonthIndex = valueChanges.index(highestChange)
        lowestMonthIndex = valueChanges.index(lowestChange)

    #Assign best and worst month
highestMonth = months[highestMonthIndex]
lowestMonth = months[lowestMonthIndex]
      
# print the Financial Analysis
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {countMonths}")
print(f'Total Profits: ${netValue}')
print(f"Average Change: ${meanValue}")
print(f"Greatest Increase in Profits:{str(highestMonth)} (${str(highestChange)})")
print(f"Greatest Decrease in Profits:{str(lowestMonth)} (${str(lowestChange)})")

#Export the file to the text file
with open(output_path, "w") as textFile:
    textFile.write("Financial Analysis")
    textFile.write("-----------------------------")
    textFile.write(f"Total Months: {countMonths}")
    textFile.write(f'Total Profits: ${netValue}')
    textFile.write(f"Average Change: ${meanValue}")
    textFile.write(f"Greatest Increase in Profits:{str(highestMonth)} (${str(highestChange)})")
    textFile.write(f"Greatest Decrease in Profits:{str(lowestMonth)} (${str(lowestChange)})")