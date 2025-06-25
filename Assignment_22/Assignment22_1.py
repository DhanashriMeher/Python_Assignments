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

    return hobj.hexdigest()  #get the result as a readable string of letters & nos(hexadecimal format).

def FindDuplicates(DirName = "Marvellous"):

    flag = os.path.isabs(DirName)

    if(flag == False):
        DirectoryName =os.path.abspath(DirName)
    #flag = os.path.exists(DirName)
    flag =os.path.exists(DirectoryName)

    #if(flag == False):
     #   print("The path is invalid")
  
    #flag = os.path.isdir(DirName)

    #if(flag == False):
     #   print("Path is valid but the target is not a directory")
      #  exit()
 
    Duplicate = {}

    for FolderName,SubFolderNames,FileNames in os.walk(DirName):
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
import smtplib
import os
from email.message import EmailMessage

def send_email1(to_email, logfile_path, stats):
    from_email = "example@gmail.com"          #  Replace with your Gmail
    app_password = " "          #  Use Gmail App Password

    # Prepare the email body safely
    if stats is None or len(stats) < 3:
        body = "Error: Could not generate statistics."
    else:
        body = f"""Duplicate File Removal Report

Start Time            : {stats[0]}
Total Files Scanned   : {stats[1]}
Duplicate Files Deleted: {stats[2]}
"""

    #  Create the email message
    msg = EmailMessage()
    msg['Subject'] = "Duplicate File Removal Report"
    msg['From'] = "example@gmail.com"
    msg['To'] = to_email
    msg.set_content(body)

    # Attach the log file
    try:
        with open(logfile_path, 'rb') as f:
            log_data = f.read()
            msg.add_attachment(log_data, maintype='application', subtype='octet-stream',
                               filename=os.path.basename(logfile_path))
    except Exception as e:
        print(f"Failed to attach log file: {e}")
        return

    # Send the email using Gmail's SMTP
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(from_email, app_password)
            server.send_message(msg)
            print(" Email sent successfully.")
    except Exception as e:
        print(f" Failed to send email: {e}")


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
    send_email1(email, logfile, stats)
    print("Duplicate files deleted and report sent.")

if __name__ == "__main__":
    main()    
