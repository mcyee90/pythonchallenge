#In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
#You will be given two sets of revenue data (budget_data_1.csv and budget_data_2.csv). Each dataset is composed of two columns:
#Date and Revenue. 
#(Thankfully, your company has rather lax standards for accounting so the records are simple.)

#Your task is to create a Python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset

# First we'll import the os module 
# This will allow us to create file paths across operating systems
import os
csvpath = os.path.join('Resources', 'budget_data_2.csv')


# # Method 1: Plain Reading of CSVs


# Method 2: Improved Reading using CSV module
import csv
with open(csvpath, newline='',encoding='utf-8') as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csvreader = list(csvreader)
    
    #print(csvreader)

    # Each row is read as a row
    
    print("Financial Analysis")
    print("------------------------------------------------")
    # --------------------------------------------------------
    # count rows
    del csvreader[0]
    # print (csvreader)

    for rows in csvreader:
        # print (rows)
        totalMonths = len(csvreader)
    print ("Total Months: " + str(totalMonths))
    
    # --------------------------------------------------------
    # get total revenue
    revenues = []
    for lines in csvreader:
        revenues.append(lines[1])
    # print (revenues)
    revs = 0
    for revLines in revenues:
        # print (revLines)
        revs = revs + int(revLines)
    print ("Total Revenue: $" + str(revs))

    #The total amount of revenue gained over the entire period

    # -------------------------------------------------------------

    # print (revenues)
    revDiff = [int(revenues[n])-int(revenues[n-1]) for n in range(1,len(revenues))]
    # print (revDiff)
    totalRevDiff = sum(revDiff)
    # print (totalRevDiff)
    avgRevDiff = totalRevDiff / len(revDiff)
    # print (avgRevDiff)
    print ("Average Revenue Difference = $" + str(avgRevDiff))
    

    #The average change in revenue between months over the entire period
    # ------------------------------------------------------------------------------------
    #The greatest increase in revenue (date and amount) over the entire period    
    # The greatest decrease in revenue (date and amount) over the entire period
    maxRev = max(revDiff)
    minRev = min(revDiff)
    # print(maxRev)
    # print(minRev)
    
    maxIndex = revDiff.index(maxRev)
    # print (maxIndex)
    csvMax = csvreader[maxIndex + 1]
    maxMonth = csvMax[0]
    # print (maxMonth)
    print ("Greatest Decrease in Revenue: " + str(maxMonth) + " ($" + str(maxRev) + ")")
    

    minIndex = revDiff.index(minRev)
    # print (minIndex)
    # print (csvreader)
    csvMin = csvreader[minIndex + 1]
    minMonth = csvMin[0]
    # print (minMonth)
    print ("Greatest Decrease in Revenue: " + str(minMonth) + " ($" + str(minRev) + ")")

    #Your final script must be able to handle any such similarly structured dataset in the future 
    #(your boss is going to give you more of these -- so your script has to work for the ones to come). 
    #In addition, your final script should both print the analysis to the terminal and export a text file with the results.

    with open('financialOutput.txt', 'w') as f:
        f.write('Financial Analysis\n')
        f.write('-----------------------------------------------\n')
        f.write('Total Months: ' + str(totalMonths) + '\n')
        f.write('Total Revenue: $' + str(revs) + '\n')
        f.write('Average Revenue Difference = $' + str(avgRevDiff) + '\n')
        f.write('Greatest Decrease in Revenue: ' + str(maxMonth) + ' ($' + str(maxRev) + ')\n')
        f.write('Greatest Decrease in Revenue: ' + str(minMonth) + ' ($' + str(minRev) + ')\n')
