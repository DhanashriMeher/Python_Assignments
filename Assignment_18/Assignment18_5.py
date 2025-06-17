#Accept file name and one string and return the frequency of that string from file.

import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Please provide names File1.txt File2.txt as command line argument")
        sys.exit()
  
    FileName = sys.argv[1]
    StrCount = sys.argv[2]

    if (os.path.exists(FileName)):
        ret = open(FileName , "r")
        data = ret.read()
        
        result = data.count(StrCount)
        print("Count :" ,result)
    
        ret.close()
    else:
        print("File not found")

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_18>python Assignment18_5.py Output.txt Learning
#Count : 2


