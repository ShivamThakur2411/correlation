import numpy as np
import csv

student_marks=[]
days_present=[]

cups_of_coffee=[]
hours_of_sleep=[]

with open("Student Marks vs Days Present.csv") as p:
    df = csv.DictReader(p)
    for row in df:
        student_marks.append(float(row["Marks In Percentage"]))
        days_present.append(float(row["Days Present"]))

with open("cups of coffee vs hours of sleep.csv") as f:
    df2 = csv.DictReader(f)
    for row in df2:
        cups_of_coffee.append(float(row["Coffee in ml"]))
        hours_of_sleep.append(float(row["sleep in hours"]))
    
    correlation1 = np.corrcoef(student_marks, days_present)
    correlation2 = np.corrcoef(cups_of_coffee, hours_of_sleep)
    print("Correlation between STUDENT MARKS and NUMBER OF DAYS PRESENT is " + str(correlation1))
    print("Correlation between CUPS OF COFFEE and HOURS OF SLEEP is " + str(correlation2))