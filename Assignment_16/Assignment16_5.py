#Write a program to read a file line by line and display those lines that contains more than 5 words.

import os
def main():
    print("Enter File name : ")
    FileName = input()
    if(os.path.exists(FileName)):
        ret = open(FileName , "r")
        data = ret.readlines()

        for line in data:
            words = len(line.split())
            if(words > 5):
                print(line.strip())

    else:
        print("File does not exists")
if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_16>python Assignment16_5.py
#Enter File name :
#data.txt
#I am learning Python ,automations and Machine Learning

#C:\Users\Dhanashri\Desktop\Python\Assignment_16>python Assignment16_5.py
#Enter File name :
#xyz.txt
#File does not exists


