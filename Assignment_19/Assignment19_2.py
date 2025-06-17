#Design automations script which accept directory name and two file extensions from 
#user.Rename all file with first file extension with second file extension

#Demo is directory. and .txt is the extension that we want to search and rename with .doc

import sys
import time
import os

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

def Validation(directory,extension1,extension2):
    if not os.path.isdir(directory):
        return FileNotFoundError(f"Directory '{directory}' does not exists")
    if not extension1.startswith(".") or not extension2.startswith("."):
        return ValueError("Extensions starts with a dot")
    return True

def Change_Extension(directory,extension1,extension2):
    count = 0
    for f in os.listdir(directory):
        if f.endswith(extension1):
            ret = os.path.splitext(f)[0]
            NewPath = ret + extension2
            OldPath = os.path.join(directory,f)
            NewPath = os.path.join(directory,ret)
            try:
                os.rename(OldPath,NewPath)
                print("New file name is : ",ret)
                count = count+1
            except Exception as e:
                print("Failed to replace extension")
    if count == 0:
        print("No files with this extension")    

def main():
    CreateLog()
    try:
        directory = input("Enter directory path: ").strip()
        ext1 = input("Enter file extension to search (e.g., .txt): ").strip()
        ext2 = input("Enter new file extension (e.g., .doc): ").strip()

        Validation(directory,ext1,ext2)
        Change_Extension(directory,ext1,ext2)

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()  

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_19>python Assignment19_2.py
#MarvellousLogTue_Jun_17_21_58_52_2025.log
#Enter directory path: C:\Users\Dhanashri\Desktop\Python\Assignment_19\Marvellous
#Enter file extension to search (e.g., .txt): .txt
#Enter new file extension (e.g., .doc): .doc
#New file name is :  Y    

        
                



    
