#Write a program which accepts file name from user and check whether that file exists in current directory or not.

import os

def main():
    print("Enter the FileName : ")
    fileName = input()
    if(os.path.exists(fileName)):
        print("File is present in the current directory")
    else:
        print("File is not present in the current directory")

if __name__ == "__main__":
    main()        
    

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_18>python Assignment18_1.py
#Enter the FileName :
#Demo.txt
#File is present in the current directory