import os
import csv

file1 = 'budget_data_1.csv'
file2 = 'budget_data_2.csv'

data_month = []
data_rev = []
data_combined = []


def sort_year(year_rev):
    return year_rev.row[0]

with open(file1, newline="", encoding='utf-8') as csvfile1:
    d1 = csv.reader (csvfile1, delimiter=',')
    next(d1)
    for row in d1:
        data_month.append(row[0])
        data_rev.append(int(row[1]))
        data_combined.append(row)

with open(file2, newline="", encoding='utf-8') as csvfile2:
    d2 = csv.reader (csvfile2, delimiter=',')
    next(d2)
    Total_Rev = 0
    Max_Rev = 0
    Prev_Max = 0
    Next_Max = 0
    Min_Rev = 0

    for row in d2:
        data_month.append(row[0])
        data_rev.append(row[1])
        data_combined.append(row)

        Total_Rev = Total_Rev + int(row[1])
        if int(row[1]) > Max_Rev: 
            Max_Rev = int(row[1])
        
data_combined.sort(key=sort_year)

Total_Months = len(data_month)
Average_Rev_Chg = round(Total_Rev/len(data_rev),0)
Greatest_Rev_Inc = Max_Rev
Greatest_Rev_Dec = 0

for i in range(len(data_combined)):
    print(data_combined[i])


print('Financial Analysis')
print('-------------------------------------------------------------')
print('Total Months: ', Total_Months)
print('Total Revenue: $', Total_Rev)  
print('Average Revenue Change: $', Average_Rev_Chg)
print('Greatest Increase in Revenue: $', Greatest_Rev_Inc)
print('Greatest Deccrease in Revenue: $', Greatest_Rev_Dec)
print(data_combined)
