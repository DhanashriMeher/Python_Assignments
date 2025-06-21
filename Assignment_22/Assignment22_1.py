#Accept Directory name from user and delete all duplicate files from the specified directory
#by considering the checksum of files.
#Create one directory as Marvellous and inside that directory create log file which
#maintains all names of duplicate files which are deleted.
#Name of that log file should contains the date and time at which thats get created
#Accpet duration in minutes from user and perform task of duplicate file removal after 
#the specific time interval
#Accpet Mail id from user and send the attachment of the log file
#Mail body should contains statistics about the operstion of duplicate file removal

#Mail bosy should contains below things:
#Starting time of scanning
#Total number of file scanned
#Total number of duplicate file found.

#Consider below command line options for script
#DuplicateFileRemoval.py E:\Data\Demo Timeinterval of script in minutes MailId

import os
import hashlib
import sys
import time
import datetime 
import smtplib
from email.message import EmailMessage

#Function to create checksum
def CalculateChecksum(path,BlockSize = 1024):
    fobj = open(path,"rb")

    hobj =hashlib.md5()

    buffer = fobj.read(BlockSize)
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer= fobj.read(BlockSize)

    fobj.close()

    return hobj.hdefexdigest()

def FindDuplicates(DirName = "Marvellous"):

    flag = os.path.isabs(DirName)

    if(flag == False):
        DirectoryName =os.path.abspath(DirName)

    flag = os.path.exists(DirName)
    
    #if(flag == False):
     #   print("The path is invalid")
  
    flag = os.path.isdir(DirName)

    #if(flag == False):
     #   print("Path is valid but the target is not a directory")
      #  exit()
 
    Duplicate = {}

    for FolderName,SubFoldeNames,FileNames in os.walk(DirName):
        for fName in FileNames:
            fName = os.path.join(FolderName,fName)
            checksum = CalculateChecksum(fName)

        if checksum in Duplicate:
            Duplicate[checksum].append(fName)
        else:
            Duplicate[checksum] = [fName]

    return Duplicate

def DeleteDuplicate(path = "Marvellous"):
    MyDict = FindDuplicates(path)
    Result = list(filter(lambda x:len(x) > 1 ,MyDict.values()))

    count = 0
    Cnt = 0

    for value in Result:
        for subvalue in value:
            count = count + 1
            if(count > 1):
                print("Deleted file : ",subvalue)
                os.remove(subvalue)
                Cnt = Cnt + 1
        count = 0

    print("Total deleted file : ",Cnt)            

#Function to send email with log
def send_email(to_email, log_path, stats):
    msg = EmailMessage()
    msg['Subject'] = "Duplicate File Removal Report"
    msg['From'] = "Example@gmail.com"  # replace
    msg['To'] = to_email
    body = f"""Duplicate File Removal Details:

Start Time         : {stats[0]}
Files Scanned      : {stats[1]}
Duplicates Deleted : {stats[2]}

See attached log for more info.
"""
    msg.set_content(body)

    with open(log_path, 'rb') as f:
        msg.add_attachment(f.read(), filename=os.path.basename(log_path))

    # Send using Gmail SMTP (change if needed)
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login("example@gmail.com","password")  # replace
        smtp.send_message(msg)

# Main function
def main():
    if len(sys.argv) != 4:
        print("Usage: DuplicateFileRemoval.py <FolderPath> <TimeInMinutes> <Email>")
        return

    folder = sys.argv[1]
    minutes = int(sys.argv[2])
    email = sys.argv[3]

    time.sleep(minutes * 60)

    os.makedirs("Marvellous", exist_ok=True)
    logfile = f"Marvellous/log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    stats = DeleteDuplicate(logfile)
    send_email(email, logfile, stats)
    print("Duplicate files deleted and report sent.")

if __name__ == "__main__":
    main()    