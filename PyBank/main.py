#First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'Budget_data.csv')
totalmonths=0
totalvalue=0
Current=0
Previous=0
Totalchanges=0
Listfordifferences=[]
num= input("how many numbers:")
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
    
        totalmonths=totalmonths+1
        totalvalue=totalvalue+int(row[1])
        Current=int(row[1])
        Change= Current-Previous
        if Previous==0:
           Previous=Current
        elif Previous!=int(Current):
          Change= Current-Previous  
          Previous=Current
          Listfordifferences.append(Change)
        if totalmonths>1:
           Totalchanges= Totalchanges+Change
Averagechange= Totalchanges/(totalmonths-1)  
Current=0
Previous=0
for amount in Listfordifferences:
    Current=amount
    if Previous==0:
        Previous=Current

    elif Current>Previous:
        greatestincrease=Current
        Previous=Current
    elif Current<Previous:
        greatestdecrease=Current
        Previous=Current
for n in (num):
      numbers=int(input("Enter number"))  
      Listfordifferences.append(numbers)

print ("financial analysis")
print ("-------------------------------------")
print ("total months: "+str(totalmonths))
print ("total: "+ str(totalvalue))
print("Average: "+str(Averagechange))
print(Listfordifferences)
print(greatestdecrease)
print(greatestincrease)
print("Greatest Increase in Profits:", max(Listfordifferences), "\nGreatest Decrease in Profits:", min(Listfordifferences))