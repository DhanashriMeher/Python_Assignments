#Schedule a job that runs every 5 minutes to write the current time to a file Marvellous.txt

import schedule
import datetime
import time

def OpenFile():
    #print("Enter FileName :")
    FileName = "Marvellous.txt"
    current_time = datetime.datetime.now()
    data = open(FileName,"a")
    data.write(str(f"{current_time}\n"))
    print(f"Current time : {current_time}")

def MySchedule():
    schedule.every(5).minutes.do(OpenFile)
    while True:
        schedule.run_pending()
        time.sleep(1)

def main():  
    OpenFile()
    MySchedule()

if __name__ == "__main__":
    main()

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_17>python Assignment17_5.py
#Current time : 2025-06-13 21:29:42.091859
#Current time : 2025-06-13 21:34:42.318175    
