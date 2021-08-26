import csv    # importing package to work with CSV - Comma Separated Value file.

def CreateCSV():
    f =open("student.csv", "w", newline='')
    csv_w=csv.writer(f, delimiter=',')

    print(choice)
    #writing a header
    fields=["rollNo", "Name", "Marks"]
    csv_w.writerow(fields)
    
    #reading data from user
    Rollno=int(input("Enter Student Roll Number:"))
    Name = input("Enter student name:")
    Marks= int(input("Enter Students marks in Comp. Sci subject:"))
    #creating a record list
    rec= [Rollno,Name,Marks]
    csv_w.writerow(rec)            # writing a rec(row) to CSV file

    f.close()


def ReadCSV():
    f =open("student.csv", "r")
    csv_r=csv.reader(f)
    
    for row in csv_r:
        print(row)
        
    for row in csv_r:
        print(','.join(row))
    
    f.close()
    

def AppendCSV():
    f =open("student.csv", "a",newline='')
    csv_w=csv.writer(f, delimiter=',')
  

    Rollno=int(input("Enter Student Roll Number:"))
    Name = input("Enter student name:")
    Marks= int(input("Enter Students marks in Comp. Sci subject:"))

    rec= [Rollno,Name,Marks]
    csv_w.writerow(rec)

    f.close()



#---------------------------------------------------------------------------------------------------------------------------
                                ####### main Program #######

ans= 'y'
while ans=='y':
    print(" **   Operations Menu  **")
    print("1. Create a CSV File.")
    print("2. Read from a CSV file.")
    print("3. Append a CSV file.")
    print("Enter 0 to Exit from the Program.")
    choice = int(input("Enter your choice:"))
    if choice == 0:
        break
    elif choice == 1:
        CreateCSV()
    elif choice == 2:
        ReadCSV()
    elif choice ==3:
        AppendCSV()
    else:
        print("Invalid Choice ... Try again..")
    
    ans=input("Do you want to perfrom more operations? Enter y for YES:")
