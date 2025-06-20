#Follow below rules while designing automation script as:
#Accept input through command line or through file.
#Display any message in log file instead of console
#For separate task define separate function
#For robustness handle every exception
#Perform validations before taking any action
#Create user defined modules to store the functionality.

#Design automation script which display information of running processes as its name,
#PID,username.

import psutil
import os
import time
import sys

def CreateLog(FolderName):
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","")  
    timestamp = timestamp.replace(":","_")      
    timestamp = timestamp.replace("/","_")   

    FileName = os.path.join(FolderName,"Marvellous%s.log"%(timestamp))   #creates file name

    fobj = open(FileName,"w")

    border = "-"*80
    fobj.write(border + "\n")
    fobj.write("Marvellous InfoSystems Process Log\n")
    fobj.write("Log file is created at : "+time.ctime()+"\n")
    fobj.write(border+ "\n")

    Data = ProcessDisplay()
    for value in Data:
        fobj.write("%s\n" %value)

    fobj.write(border + "\n")    
   

def ProcessDisplay():
    Border = "*"*25
    print(Border +"\n")
    print("Information of currently running Processes ")
    print(Border+"\n")

    listProcess=[]

    for process in psutil.process_iter():
        try:
            info = process.as_dict(attrs=['pid','name','username'])
            listProcess.append(info)
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass    
        
    return listProcess   


def main():
    if len(sys.argv) > 2:
        print("Please give accurate command line argument.")
    else:
        data= sys.argv[1]
    CreateLog(data)
    ProcessDisplay()

if __name__ == "__main__":
    main()




