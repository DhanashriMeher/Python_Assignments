#Write a python script to count the number of lines ,words and characters in a given file.

import os

def main():
    print("FileName is : ")
    FileName = input()
    if (os.path.exists(FileName)):
        data= open(FileName,"r")
       
        lines = data.readlines()

        line_count = len(lines)
        word_count  = 0
        char_count = 0

        for line in lines :
            word_count = word_count + len(line.split())
            char_count = char_count + len(line)

        print("Count the lines of Files : " ,line_count)
        print("Count of Words : ",word_count)
        print("Count of characters : ",char_count)

    else:
        print("File not exist")    

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_16>python Assignment16_3.py
#FileName is :
#Student.txt
#Count the lines of Files :  7
#Count of Words :  14
#Count of characters :  80