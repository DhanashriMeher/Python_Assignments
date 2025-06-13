#Write a python program to create a text file named student.txt and write the names of 5 students into it.

import os

def main():
    print("Enter The filename to check it is present or not")
    FileName = input()
    ret = os.path.exists(FileName)

    if (ret == True):
        ("File present in the directory")

    result = open(FileName ,"w")
    result.write("\nName of Students :\n")
    stud = ["Kedar Pate\n","Sanjay Sarode\n","Lokesh Patil\n","Vinay Oswal\n","Tanay Oak\n"]
    result.writelines(stud)

    print("Five student names added")

    result = open(FileName,"r")
    data = result.read()
    print(data)

if __name__ == "__main__":
    main()

#OUTPUT
#Enter The filename to check it is present or not
#student.txt
#Five student names added

#Name of Students :
#Kedar Pate
#Sanjay Sarode
#Lokesh Patil
#Vinay Oswal
#Tanay Oak
