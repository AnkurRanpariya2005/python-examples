import pickle

def Createfile():
    # to create a link with a file
    file = open("student.dat","wb")
    
    #getting inputs
    rno = int(input("Enter roll no of student:"))
    Name = input("Enter name of the Student:")
    marks= eval(input("Enter marks in comp. sci. subject (out of 40):"))
    
    #insetring object into structure data 
    stu= [rno, Name,marks]
    
    # dumping / pickling stu object to a file.
    pickle.dump(stu,file)
    print("File created ....")
    
    # closing a link with a file.
    file.close()

def Appendfile():
    # to create a link with a file
    file = open("student.dat","ab")
    
    #getting inputs
    rno = int(input("Enter roll no of student:"))
    Name = input("Enter name of the Student:")
    marks= eval(input("Enter marks in comp. sci. subject (out of 40):"))
    
    #insetring object into structure data 
    stu= [rno, Name,marks]
    
    # dumping / pickling stu object to a file.
    pickle.dump(stu,file)
    print("File created ....")
    
    # closing a link with a file.
    file.close()

def Readfile():
    file = open("student.dat","rb")
    try:
        while True:
            stu= pickle.load(file)
            print(stu)
    except EOFError:
        pass
        
    file.close()


def Searchfile():
    file = open("student.dat","rb")
    rol=int(input("Enter roll no. to be search in the file:"))
    flag=0
    try:
        while True:
            stu= pickle.load(file)
            if stu[0]==rol:
                print("Roll No.:",stu[0])
                print("Name:",stu[1])
                print("Marks In CS:",stu[2])
                flag=1
                break
    except EOFError:
        pass
    if flag == 0:
        print("Record not found in the file.")
    file.close()
    
    
def Deleterec1():
    rno = int(input("Enter a roll no you want to delete:"))
    rfile = open("student.dat","rb")
    reclst= []
    flag =0
    try:
        while True:
            rec = pickle.load(rfile)
            reclst.append(rec)
    except EOFError:
        pass
    rfile.close()
    #print(reclst)

    wfile= open("student.dat","wb")
    
    for rec in reclst:
        if rec[0]== rno:
           flag =1
           print("record found and deleted..")
           continue
        else:
           pickle.dump(rec,wfile)
     
    wfile.close()
    if flag == 0:
        print("Record not found in the file.")



def Deleterec():
     import os
     rno = int(input("Enter a roll no you want to delete:"))
     rfile = open("student.dat","rb")
     wfile = open("temp.dat","wb")
     flag =0
     try:
         while True:
             rec = pickle.load(rfile)
             if rec[0]== rno:
                 flag =1
                 print("record found & deleted.")
                 continue
             else:
                 pickle.dump(rec,wfile)
     except EOFError:
        pass
     rfile.close()
     wfile.close()
    
     os.remove("student.dat")
     os.rename("temp.dat","student.dat")
    
     if flag ==0:
        print("Record not found....")
    
                 

'''###   ..................... ######'''
ans = 'y'
while ans =='y':
    print("Program menu to work with a binary file")
    print("1. TO create a File.")
    print("2. To append a file.")
    print("3. To read from a file.")
    print("4. To search in binary file.")
    print("5. To  Delete a record from a file.")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        Createfile()
    elif choice == 2:
        Appendfile()
    elif choice == 3:
        Readfile()
    elif choice == 4:
        Searchfile()
    elif choice == 5:
        Deleterec()
    else:
        print("Invalid choice ...")
    
    ans = input("Do you want to perfrom operations? Enter y for YES):")