# Import modules
import os
import csv
# Read in csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    # print(f"Header: {header}")
    date = []
    revenue = []
    change = []
    total=0
    totalamt = 0
    for row in csvreader:
        date.append(row[0])
        revenue.append(float(row[1]))

        # The total number of months included in the dataset
        total=total+1

        # The total net amount of "Profit/Losses" over the entire period
        totalamt=totalamt+int(row[1])
    for i in range(1,total):
        change.append(revenue[i] - revenue[i-1])
        # The average change in "Profit/Losses" between months over the entire period  
        average = round(sum(change)/len(change),2)
        # The greatest increase in profits (date and amount) over the entire period 
        increase = round(max(change))
        increase_date = str(date[change.index(max(change))])
        # The greatest decrease in losses (date and amount) over the entire period
        decrease = round(min(change))
        decrease_date = str(date[change.index(min(change))])

    # Print out Financial Analysis to terminal and text file
    print (f"Financial Analysis")
    print (f"----------------------------")
    print (f"Total months: {total}")
    print (f"Total: ${str(totalamt)}")
    print (f"Average Change: ${str(average)}")
    print (f"Greatest Increase in Profits: {increase_date} (${str(increase)})")
    print (f"Greatest Decrease in Profits: {decrease_date} (${str(decrease)})")
    text_file = open("fin_analysis.txt","w")
    with open("fin_analysis.txt", "w") as text_file:
        print (f"Financial Analysis", file=text_file)
        print (f"----------------------------", file=text_file)
        print (f"Total months: {total}", file=text_file)
        print (f"Total: ${str(totalamt)}", file=text_file)
        print (f"Average Change: ${str(average)}", file=text_file)
        print (f"Greatest Increase in Profits: {increase_date} (${str(increase)})", file=text_file)
        print (f"Greatest Decrease in Profits: {decrease_date} (${str(decrease)})", file=text_file)
    text_file.close()