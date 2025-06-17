#Design automation script which accept directory name and write names of duplicate files 
#from that directory into log file named as Log.txt.
#Log.txt file should be created into current directory.

import os
import hashlib
import time

def CreateLog():
    timestamp = time.ctime()

    fileName = "MarvellousLog%s.log" %timestamp
    fileName = fileName.replace(" ","_")
    fileName = fileName.replace(":","_")

    print(fileName)

    fobj = open(fileName ,"w")
    Border = "_ _"*54
    fobj.write(Border+"\n")
    fobj.write("This is a log File of Automation Script\n")
    fobj.write(Border+"\n")

    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    fobj.write(Border+"\n")
    fobj.write("This is a created at \n "+timestamp+"\n")
    fobj.write(Border+"\n")

def Validation(directory):
    if not os.path.isdir(directory):
        return FileNotFoundError(f"Directory '{directory}' does not exists")

def CalculateChecksum(FileName):
    try:
        fobj = open(FileName , "rb")  #reading binary code

        hobj = hashlib.md5()  #md5 class object created

        buffer = fobj.read(1024)  #1KB = 1024 bytes
        while(len(buffer)> 0):
            hobj .update(buffer)
            buffer = fobj.read(1024)

        #fobj.close()

        #print("Checksum of file is : ",hobj.hexdigest())  #inbuilt function gives 32 bytes number

    except Exception as e:
        print(f"Failed to read file")
        return None
    
def findDuplicates(dir):
    checksumarr={}
    for file in os.listdir(dir):
        path = os.path.join(dir,file) 
        if os.path.isfile(path):
            checksum = CalculateChecksum(path)
            if checksum:
                if checksum in checksumarr:
                    print("Duplicate found")
                else:
                    print("Duplicate not found")    
def main():
    CreateLog()
    try:
        directory = input("Enter directory path: ").strip()
        Validation(directory)
        findDuplicates(directory)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
