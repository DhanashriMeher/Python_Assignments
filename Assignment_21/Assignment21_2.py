#Design automation script which accept process name and display information of that
#process if it is running.

import os
import sys
import time
import psutil

def Createlog():
    
    timestamp = time.ctime()
    timestamp = timestamp.replace(" ","_")
    timestamp = timestamp.replace(".","_")
    timestamp = timestamp.replace("/","_")

    #FileName = os.path.join(FolderName,"Assignment2Log%s.log"%(timestamp))

    FileName = "Assignment21_2log.txt"
    fobj = open(FileName ,"w")

    Border = "*"*80
 
    fobj.write(Border + "\n")
    fobj.write("Log File of Assignment21_2\n")
    fobj.write("this log is created at : " +time.ctime()+ "\n")
    fobj.write(Border + "\n")

    if len(sys.argv) < 2:
        print("Please use command line argument")
    else:
        pname = sys.argv[1]
        data = RunningProcess(pname)
        if data is not None:
          for value in data:    
             fobj.write("%s\n" %value)
    fobj.write(Border + "\n")    
            
def RunningProcess(name):
    for proc in psutil.process_iter(['pid','name']):
        if proc.info['name'] and name.lower() in proc.info['name'].lower():
            print(f"Process found : PID = {proc.info['pid']},Name = {proc.info['name']}")
            return 
    print(f"No running process found with name: {name}\n")
    
def main():
    Createlog()

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_21>python Assignment21_2.py chrome.exe
#Process found : PID = 7560,Name = chrome.exe