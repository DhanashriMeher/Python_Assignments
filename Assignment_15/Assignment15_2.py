#Write a program which accepts file name from user and open that file and display that contents of that file on screen.
#Input : Demo.txt
#Display contents of Demo.txt on console.

import os

def main():
    print("Enter the file name you want to check : ")
    FileName = input()
    result = os.path.exists(FileName)

    if(result == True):
        print("File is present in current directory")
        fobj = open(FileName,"r")
        data = fobj.read()

        print("Data from file is : ",data)

        fobj.close()
    else:
        print("There is no such file found in directory")  

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_15>python Assignment15_2.py
#Enter the file name you want to check :
#Demo.txt
#File is present in current directory
#Data from file is :
#Hi
#My name is Dhanashri . !!!!