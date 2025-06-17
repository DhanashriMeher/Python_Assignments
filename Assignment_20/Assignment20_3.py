#Design Automation script which accept directory name and delete all duplicate files from 
#that directory. Write names of duplicate files from that directory into log File named as Log.txt
#as Log.txt.  
#Log.txt should be created into current directory

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

# Validate the directory
def validate_directory(directory):
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist.")

# Calculate checksum of a file using SHA256
def calculate_checksum(file_path):
    try:
            fobj = open(file_path , "rb")
            hobj = hashlib.md5()
            buffer = fobj.read(1024)  #1KB = 1024 bytes
            while(len(buffer)> 0):
                 hobj .update(buffer)
                 buffer = fobj.read(1024)

            return hobj.hexdigest()
    except Exception as e:
        print(f"Cannot read file {file_path}: {e}")
        return None

# Find and delete duplicate files
def delete_duplicates(directory):
    checksum_map = {}
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            checksum = calculate_checksum(file_path)
            if checksum:
                if checksum in checksum_map:
                    # Duplicate found, delete the file
                    try:
                        os.remove(file_path)
                        print(f"Deleted duplicate: {file}")
                    except Exception as e:
                        print(f"Failed to delete {file}: {e}")
                else:
                    checksum_map[checksum] = file

# Main function
def main():
    CreateLog()
    try:
        directory = input("Enter directory path: ").strip()
        validate_directory(directory)
        delete_duplicates(directory)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_20>python Assignment20_3.py Automation
#MarvellousLogWed_Jun_18_00_06_25_2025.log
#Enter directory path: C:\Users\Dhanashri\Desktop\Python\Assignment_20\Automation
#Deleted duplicate: x (2).txt
#Deleted duplicate: x.txt
#Deleted duplicate: y.txt    
