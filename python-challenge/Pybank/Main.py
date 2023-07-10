import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

date=[]
profit_losses=[]
headers=[]
Difference=[]

#Purpose: read the csv, skip and store header, appending lists (row is column)
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headers = next(csvreader)
    for row in csvreader: 
        date.append(row[0])
        profit_losses.append(int(row[1]))

for imaginary_thing in profit_losses:
                     #next address                #current address
    difference = profit_losses[imaginary_thing + 1] - profit_losses[imaginary_thing]
    Difference.append(int(difference))
#calculate total number of months included in list
Total_Months = len(date)

#calculate net total amount of Profit/losses
Net_total=sum(profit_losses)







