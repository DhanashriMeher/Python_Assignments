#Design Automation script which accept two directory names. Copy all Files from first
#Directory into second directory.Second directory should be created at run time
#Demo is name of directory which is existing and contains files in it.We have to 
#Create as temp and copy all files from Demo to temp

import os
import sys
import shutil
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
    
def CopyFile(directory1,directory2):
    count = 0
    for f in os.listdir(directory1):
        OldPath = os.path.join(directory1,f)
        NewPath = os.path.join(directory2,f)
        if os.path.isfile(OldPath):
            try:
                shutil.copy2(OldPath,NewPath)
                print(f"copied : {f}")
                count = count+1
            except Exception as e:
                print("Failed to replace")
    if count == 0:
        print("No directory with this name")    

def main():
    CreateLog()
    try:
        directory1 = input("Enter directory(eg.Demo) : ").strip()
        directory2 = input("Enter directory(eg.Temp) : ").strip()

        Validation(directory1)
        CopyFile(directory1,directory2)

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()  

 #OUTPUT
 # C:\Users\Dhanashri\Desktop\Python\Assignment_19>python Assignment19_4.py
#MarvellousLogTue_Jun_17_22_57_44_2025.log
#Enter directory(eg.Demo) : Demo
#Enter directory(eg.Temp) : Temp
#copied : Abc.exe
#copied : abc.txt
#copied : x.txt   
