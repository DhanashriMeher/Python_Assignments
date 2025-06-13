#Write a script to remove all blank lines from a file.Save the cleaned output to a new file

import os

def main():
    print("Enter a file name : ")
    FileName = input()

    print("Enter a file name in which data need to copy :")
    FileName1 = input()
    if(os.path.exists(FileName)): 
        result = open(FileName , "r")
        ret = open(FileName1,"w")
        for i in result :
            data = i.strip()
            ret.write(data)
        print("Cleaned the blank lines and whitespaces")
    else:
        print("There is no such file exist")

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_16>python Assignment16_8.py
#Enter a file name :
#input.txt
#Enter a file name in which data need to copy :
#output.txt
#Cleaned the blank lines and whitespaces


