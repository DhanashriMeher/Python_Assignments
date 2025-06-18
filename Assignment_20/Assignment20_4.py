#Design automation script which accept directory name and delete all duplicate files from that
#directory. Write names of duplicate files from that directory into log file named as
#Log.txt. Log.txt should be created into current directory.Display execution time 
#required for the script.

import os
import hashlib
import time

def CreatLog():
    timestamp = time.ctime()

    fileName = "MarvellousLog%s.log" %timestamp 
    fileName = fileName.replace(" ","_")
    fileName = fileName.replace(":","_")

    print(fileName)

    fobj =open(fileName,"w")
    Border = "**"*60
    fobj.write(Border + "\n")
    fobj.write("This is log File for automation script\n")
    fobj.write(Border + "\n")

    fobj.write("\n\n\n\n\n\n\n\n\n\n\n")

    fobj.write(Border+"\n")
    fobj.write("This is created at \n" +timestamp+ "\n")
    fobj.write(Border+"\n")

#Validate the directory
def Validate_directory(dirname):
    if not os.path.isdir(dirname):
        return FileNotFoundError(f"Directory '{dirname}' does not exist.")
    
#Calculate checksum of file using md5
def calculate_checksum(file_Path):
    try:
        fobj = open(file_Path,"rb")
        hobj = hashlib.md5()
        buffer = fobj.read(1024)
        while(len(buffer)>0):
            hobj.update(buffer)
            buffer=fobj.read(1024)

        return hobj.hexdigest()
    except Exception as e:
        print(f"Cannot read file {file_Path}: {e}")

#Find and  delete duplicate file
def DuplicateFiles(directory):
    checksumarr = {}
    for file in os.listdir(directory):
        file_path = os.path.join(directory,file)
        if os.path.isfile(file_path):
            checksum = calculate_checksum(file_path)
            if checksum:
                if checksum in checksumarr:
                    try:
                        os.remove(file_path)
                        print(f"Deleted Files : {file}")
                    except Exception as e:
                        print(f"Failed to delete {file}: {e}")
                else:
                    checksumarr[checksum] = file

#Main function
def main():
    CreatLog()
    try:
        directory = input("Enter directory path : ").strip()
        Validate_directory(directory)
        start_time = time.time()
        DuplicateFiles(directory)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Script executed in {execution_time:.2f} seconds")

    except Exception as e:
        print(f"Error : {e}")

if __name__ == "__main__":
    main()

#C:\Users\Dhanashri\Desktop\Python\Assignment_20>python Assignment20_4.py Marvellous
#MarvellousLogWed_Jun_18_21_00_57_2025.log
#Enter directory path : C:\Users\Dhanashri\Desktop\Python\Assignment_20\Automation
#Deleted Files : x (2).txt
#Deleted Files : x.txt
#Deleted Files : y.txt
#Script executed in 0.07 seconds    
                 










