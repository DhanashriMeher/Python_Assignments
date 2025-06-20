#Design Automation script which accept directory name and mail id from user and create log file im that
#in that directory which contains information of running processes as its name,PID,Username.
#After creating log file send that log file to the specified mail.


import os
import psutil
import time
import smtplib
from email.message import EmailMessage

def Createlog(FolderName):
    
    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","_")
    timestamp = timestamp.replace(".","_")
    timestamp = timestamp.replace("/","_")

    FileName = os.path.join(FolderName,"Assignment21_4processlog.txt")

    fobj = open(FileName ,"w")

    Border = "*"*80
 
    fobj.write(Border + "\n")
    fobj.write("Log File of Assignment21_4\n")
    fobj.write("this log is created at : " +time.ctime()+ "\n")
    fobj.write(Border + "\n")

    data = RunningProcess()
    if data is not None:
        for value in data:    
            fobj.write("%s\n" %value)
    fobj.write(Border + "\n")    
      

def RunningProcess():
    listProcess=[]

    for process in psutil.process_iter():
        try:
            info = process.as_dict(attrs=['pid','name','username'])
            listProcess.append(info)   
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass    
    return listProcess    

def send_mail(sender, password, receiver, file_path):
    msg = EmailMessage()
    msg['Subject'] = 'Process Log'
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content("Attached is the process log file.")

    f = open(file_path, "rb")
    msg.add_attachment(f.read(), maintype='text', subtype='plain', filename="process_log.txt")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender, password)
        server.send_message(msg)

        
def main():
    email = input("Enter receiver email: ")
    logfile = "Assignment21_4log.txt"


    pname = "Automation"
    if not os.path.exists(pname):
        os.makedir(pname)
        print("Invalid Directory")
        return

    Createlog(pname)
  
    #sender = ""
    #password = ""

   # send_mail(sender, password, email, logfile)
    print("Log file sent successfully.")

if __name__ == "__main__":
    main()
