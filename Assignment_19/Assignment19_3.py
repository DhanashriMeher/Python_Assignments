#Design Automation script which accept two directory names and one file extension.Copy all
#Files with the specified extension from first directory into second diretory.
#Second directory should be created at run time.
#Usage :DirectoryCopyExt/py "Demo""Temp"".exe"
#Demo is name of directory which is existing and contains files in it.We have to 
#Create as temp and copy all files with extension.exe from Demo to temp

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

def Validation(directory,extension):
    if not os.path.isdir(directory):
        return FileNotFoundError(f"Directory '{directory}' does not exists")
    if not extension.startswith("."):
        return ValueError("File extension must start with a dot")
    return True

def CopyFile(directory1,directory2,extension):
    count = 0
    for f in os.listdir(directory1):
        if f.endswith(extension):
            OldPath = os.path.join(directory1,f)
            NewPath = os.path.join(directory2,f)
            try:
                shutil.copy2(OldPath,NewPath)
                print(f"copied : {f} to {directory2}" )
                count = count+1
            except Exception as e:
                print("Failed to replace extension")
    if count == 0:
        print("No files with this extension")    

def main():
    CreateLog()
    try:
        if len(sys.argv) != 4:
            raise ValueError("Please use <source_dir> <dest_dir> <extension> as a command line argument")

        directory1 = sys.argv[1].strip()
        directory2 = sys.argv[2].strip()
        ext2 = sys.argv[3].strip()

        Validation(directory1,ext2)
        CopyFile(directory1,directory2,ext2)

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()  

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_19>python Assignment19_3.py Demo Temp .exe
#MarvellousLogTue_Jun_17_22_59_06_2025.log
#copied : Abc.exe to Temp    
