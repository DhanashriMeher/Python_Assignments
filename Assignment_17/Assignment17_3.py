#Write a program that schedules a function to print "do coding.....!" every 30 minutes

import schedule
import time

def MySchedule():
    print("Do coding......!")

def main():
    schedule.every(30).minutes.do(MySchedule)

    while(True):
        schedule.run_pending()
        time.sleep(1)    

if __name__ == "__main__":
    main()
