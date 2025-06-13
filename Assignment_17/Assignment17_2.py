#Schedule a task that displays the current date and time every minute using the datetime
#module.

import schedule
import datetime
import time

def MySchedule():
    print("Inside MySchedule Function at : ",datetime.datetime.now())

def main():
    print("Inside automation script : ")

    schedule.every(1).minutes.do(MySchedule)

    while(True):
        schedule.run_pending()
        time.sleep(2)

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_17>python Assignment17_2.py
#Inside automation script :
#Inside MySchedule Function at :  2025-06-13 18:04:36.901762
#Inside MySchedule Function at :  2025-06-13 18:05:36.944756
#Inside MySchedule Function at :  2025-06-13 18:06:36.973124