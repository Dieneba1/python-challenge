#First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'Election_Data.csv')
totalnumberofvotes=0
votespercentage=0
votespercandidate=0
Listofcandidates=[]


with open(csvpath) as csvfile:

 # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:

        totalnumberofvotes=totalnumberofvotes +1
        Listofcandidates.append(row[1])
print ("Election Results")
print ("-------------------------------------")
print ("total Votes: "+str(totalnumberofvotes))
print ("-------------------------------------")
