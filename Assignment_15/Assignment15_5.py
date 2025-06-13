#Accept file name and one string from user. and return the frequency of that string from file.
#Input : Demo.txt  Marvellous
#Search "Marvellous in Demo.txt"

import os
import sys

def main():
    if len(sys.argv) !=3 :
        print("Please run code properly")
        sys.exit()

    FileName = sys.argv[1]
    FileName1 = sys.argv[2]

    if (os.path.exists(FileName)):
        ret = open(FileName , "r")
        data = ret.read()
        
        result = data.count(FileName1)
        print("Count" ,result)
    
        ret.close()
    else:
        print("File not found")

if __name__ == "__main__":
    main()

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_15>python Assignment15_5.py ABC.txt Marvellous
#Count 2    

    
