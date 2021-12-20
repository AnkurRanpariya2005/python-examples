import csv
f = open("student.csv","a",newline='')  #EOL inserted by os
wcsv= csv.writer(f)
#Getting inputs from the user
Rno = int(input("Enter Student Rollno:"))
Nam=input("Enter Student Name:")
marks=int(input("Enter marks in CS subject (out of 40):"))
stu = [Rno,Nam,marks]
wcsv.writerow(stu)
print("rec. written in csv file.")
f.close()
