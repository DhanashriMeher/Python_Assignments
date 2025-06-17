#Follow below rules while designing automation script as:
#Accept input through command line or through file.
#Display any message in log file instead of console
#For separate task define separate function
#For robustness handle every exception
#Perform validations before taking any action
#Create user defined modules to store the functionality.

#Design Automation script which accept directory name and file extension from user.
#Display all files with that extension.

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

def Validation(directory,extension):
    if not os.path.isdir(directory):
        return FileNotFoundError(f"Directory '{directory}' does not exists")
    if not extension.startswith("."):
        return ValueError("File extension must start with a dot")
    return True

def readDir():
    if len(sys.argv) >=3 :
        return sys.argv[1],sys.argv[2]
    else:
        DirName = input("Enter directory path :")
        Dir_ext = input("Enter file extension : ")
        return DirName.strip(),Dir_ext.strip()
    
def file_Extension(directory,extension):
    files = []
    for f in os.listdir(directory):
        if f.endswith(extension):
            files.append(f)
    return files            
    
def main():
    CreateLog()
    try:
        directory,extension = readDir()
        Validation(directory,extension)

        Result = file_Extension(directory,extension)
        if Result:
            for file in Result:
                print(f"Found file :\n {Result}")
        else:
            print(f"No files found with extension{extension} in {directory}")        

    except Exception as e:
        print(f"Error occurred: {str(e)}")
    
if __name__ == "__main__":
    main()
#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_19>python Assignment19_1.py
#MarvellousLogTue_Jun_17_21_02_09_2025.log
#Enter directory path :C:\Users\Dhanashri\Desktop\Python\Automations\Marvellous
#Enter file extension : .txt
#No files found with extension.txt in C:\Users\Dhanashri\Desktop\Python\Automations\Marvellous

#C:\Users\Dhanashri\Desktop\Python\Assignment_19>python Assignment19_1.py
#MarvellousLogTue_Jun_17_21_03_07_2025.log
#Enter directory path :C:\Users\Dhanashri\Desktop\Python\Automations\Marvellous
#Enter file extension : x.txt
#Found file :
# ['x.txt']