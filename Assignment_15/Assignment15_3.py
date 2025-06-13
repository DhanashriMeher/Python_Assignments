#Write a program which accepts file name from user and create new file named as Demo.txt and copy all contents from existing file into new file 
#Accept file name through command line arguments.

#Input : ABC.txt
#Create new file as Demo.txt and copy all contents of ABC.txt in Demo.txt.

import os
import sys

def main():

   #Check if user's gave file name or not
    if len(sys.argv)!= 2 :
        print("Please run code properly")
        sys.exit()

    #Get the file name from command line.
    FileName = sys.argv[1]

    #Check file exists or not.
    if os.path.exists(FileName):
        print("File exists")
    else :
        print("File does not exists")
        sys.exit()

    #open file and read content
    result = open(FileName ,'r')
    data = result.read()
 
    #Create Demo.txt and copied data into it.
    ret = open("Demo1.txt",'w')
    ret.write(data)

    print("Content copied to Demo1.txt")

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_15>python Assignment15_3.py ABC.txt
#File exists
#Content copied to Demo1.txt