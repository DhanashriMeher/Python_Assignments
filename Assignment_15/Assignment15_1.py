#Write a program which accepts file name from user and check whether that file exists in current directory or not.
#Input : Demo.txt
#check whether Demo.txt exists or not.

import os

def main():
    print("Enter the name of file that want to check : ")
    Filename = input()

    result = os.path.exists(Filename)

    if(result == True):
        print("File is present in current directory")
    else : 
        print("There is no such file")    


if __name__ == "__main__":
    main()

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_15>python Assignment15_1.py
#Enter the name of file that want to check :
#Demo.txt
#File is present in current directory    