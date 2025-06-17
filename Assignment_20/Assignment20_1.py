#Follow below rules while designing automation script as:
#Accept input through command line or through file.
#Display any message in log file instead of console
#For separate task define separate function
#For robustness handle every exception
#Perform validations before taking any action
#Create user defined modules to store the functionality.

#Design automation script which accept directory name and display checksum of all files

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

        fobj.close()

        print("Checksum of file is : ",hobj.hexdigest())  #inbuilt function gives 32 bytes number

    except Exception as e:
        print(f"Failed to read file")
        return None
    
def Directory1(dir):
    files = os.listdir(dir)
    if not files:
        print("No files found in dirctory")
        return

    for file in files:
        path = os.path.join(dir,file) 
        if os.path.isfile(path):
            checksum = CalculateChecksum(path)
            if checksum:
                print(f"{file}:{checksum}")

def main():
    CreateLog()
    try:
        directory = input("Enter directory path: ").strip()
        Validation(directory)
        Directory1(directory)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_20>python Assignment20_1.py
#Enter directory path: C:\Users\Dhanashri\Desktop\Python\Assignment_20\Automation
#Checksum of file is :  d41d8cd98f00b204e9800998ecf8427e
#Checksum of file is :  d41d8cd98f00b204e9800998ecf8427e    
    
