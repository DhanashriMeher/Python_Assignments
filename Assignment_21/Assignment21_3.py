#Design Automation script which accept directory name from user and create log file in that directory
#which contains information of running processes as its name ,PId,username.

import os
import psutil
import time

def Createlog(FolderName):
    
    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","_")
    timestamp = timestamp.replace(".","_")
    timestamp = timestamp.replace("/","_")

    FileName = os.path.join(FolderName,"process_log.txt")

    fobj = open(FileName ,"w")

    Border = "*"*80
 
    fobj.write(Border + "\n")
    fobj.write("Log File of Assignment21_3\n")
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
        
def main():
  #  if len(sys.argv) < 2:
   #     print("Please use command line argument")
    #    return
    
    #pname = sys.argv[1]
    pname = "Automation"
    if not os.path.exists(pname):
        os.makedir(pname)
        print("Invalid Directory")
        return

    Createlog(pname)

if __name__ == "__main__":
    main()
