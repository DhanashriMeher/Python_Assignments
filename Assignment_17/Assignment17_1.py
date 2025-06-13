#Write a python script that prints "Jay Ganesh ..." every  seconds.Use the schedule.
#every(2).seconds.do(...)function.

import schedule
import time

def MySchedule():
    print("Jay Ganesh...")

def main():
    print("Inside automation script : ")

    schedule.every(2).seconds.do(MySchedule) 

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_17>python Assignment17_1.py
#Inside automation script :
#Jay Ganesh...
#Jay Ganesh...
#Jay Ganesh...
#Jay Ganesh...
#Jay Ganesh...
#Jay Ganesh...
   