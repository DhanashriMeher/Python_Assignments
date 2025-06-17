#Write a program which accept two file names from user and compare contents of both the files.If both the files contains same 
#contents then display success otherwise dosplay failure.Accept names of both the files from command line.

import sys
import os
import filecmp

def main():
    if len(sys.argv) < 2:
        print("Please provide names File1.txt File2.txt as command line argument")
  
    File1 = sys.argv[1]
    File2 = sys.argv[2]

    if os.path.exists(File1):
        if os.path.exists(File2):
            Compare_File = filecmp.cmp(File1,File2)
            if Compare_File:
                print("Success")
            else:
                print("Failure")     
        else:
            print("File2 is not present in the directory")    
    else:
        print("File1 is not present in the directory")

if __name__ =="__main__":
    main()    

#OUTPUT    
#C:\Users\Dhanashri\Desktop\Python\Assignment_18>python Assignment18_4.py Abc.txt xyz.txt
#File2 is not present in the directory

#C:\Users\Dhanashri\Desktop\Python\Assignment_18>python Assignment18_4.py xyz.txt Abd.txt
#File1 is not present in the directory

#C:\Users\Dhanashri\Desktop\Python\Assignment_18>python Assignment18_4.py Abc.txt Output.txt
#Success
