#Write a program which accepts two file name from user and compare contents of both the files.If both the files contains same contents
#then display success otherwise display failure.Accept names of both the files from command lines

#Input : Demo.txt   Hello.txt
#compare contents of Demo.txt and Hello.txt

import sys
import os

def main():
    if len(sys.argv)!= 3:
        print("Enter name properly")
        sys.exit()

    FileName = sys.argv[1]
    FileName2 = sys.argv[2]

    if(os.path.exists(FileName) and os.path.exists(FileName2)):
        result = open(FileName ,"r").read()
        result1= open(FileName2 , "r").read()
        if result == result1 :
            print("Success")
        else :
            print("Failure") 
    else:
        print("File not exists")

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_15>python Assignment15_4.py ABC.txt Demo1.txt
#Success

#C:\Users\Dhanashri\Desktop\Python\Assignment_15>python Assignment15_4.py ABC.txt Demo.txt
#Failure



    

               