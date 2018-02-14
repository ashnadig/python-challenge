
import os
import csv
import datetime

file1 = 'employee_data1.csv'
file2 = 'employee_data2.csv'
EmpOutputCSV = 'employee_data3.csv'

Combined_Emp_data = os.path.join('', 'Combined_Emp_Data' + '.csv')
file3 = 'Combined_Emp_Data.csv'

Emp_L1 = []
Emp_Id = []
Emp_LName = []
Emp_FName = []
Emp_Name = []
Emp_DOB = []
Emp_SSN = []
Emp_State = []
clean_list = []


with open(file1, newline="", encoding='utf-8') as csvfile1:
    d1 = csv.reader (csvfile1, delimiter=',')
    next(d1)
    for row in d1:
       Emp_L1.append(row)
    

with open(file2, newline="", encoding='utf-8') as csvfile2:
    d2 = csv.reader (csvfile2, delimiter=',')
    next(d2)
    for row in d2:
       Emp_L1.append(row)

with open(Combined_Emp_data, 'w', newline="") as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=',')
        # Write Headers into file
        csvWriter.writerow(["Emp ID","Name","DOB","SSN","State"])
        # Write the zipped lists to a csv
        csvWriter.writerows(Emp_L1)

with open(file3, newline="", encoding='utf-8') as csvfile3:
    d3 = csv.reader (csvfile3, delimiter=',')
    
    for row in d3:
        Emp_Id.append(row[0])
        Emp_Name.append(row[1])
        Emp_DOB.append(row[2])
        Emp_SSN.append(row[3])
        Emp_State.append(row[4])

        Emp_FName.append(row[1][0])
        Emp_LName.append(row[1])

clean_list = zip(Emp_Id,Emp_FName,Emp_LName, Emp_DOB, Emp_SSN, Emp_State)

with open(EmpOutputCSV, 'w', newline="") as newcsv:
    newcsvwriter = csv.writer(newcsv, delimiter=',')

    newcsvwriter.writerow(["Emp ID","FirstName","LastName","DOB","SSN","State"])
    newcsvwriter.writerows(clean_list)
# Mask SSN number except last four digits
mask_ssn = "Emp_SSN"
ssnlength = len(mask_ssn)
masked = ssnlength - 4
slimstr = mask_ssn[masked:]
#print("*" * masked + slimstr)
