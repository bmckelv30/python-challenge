# Import modules
import os
import csv
# Read in csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Read in the CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    # print(f"Header: {header}")
    # use of next to skip first title row in csv file
    date = []
    revenue = []
    change = []
    total=0
    for row in csvreader:
        date.append(row[0])
        revenue.append(float(row[1]))
        total=total+1
    
        #in this loop I did total of difference between all row of column "Revenue" and found total revnue change. Also found out max revenue change and min revenue change. 
    for i in range(1,total):
        change.append(revenue[i] - revenue[i-1])   
        average = round(sum(change)/len(change),2)
        increase = round(max(change))
        decrease = round(min(change))
        increase_date = str(date[change.index(max(change))])
        decrease_date = str(date[change.index(min(change))])

        print (f"Financial Analysis")
        print (f"----------------------------")
        print (f"Total months: {total}")
        print (f"Average Change: ${str(average)}")
        print (f"Greatest Increase in Profits: {increase_date} (${str(increase)})")
        print (f"Greatest Decrease in Profits: {decrease_date} (${str(decrease)})")