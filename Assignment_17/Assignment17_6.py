#Write a script that schedules multiple task : one to print "Lunch Time !!"at 1 PM
#And another to print "Wrap up work" at 6 PM

import time
import schedule

def FirstSchedule():
    print("Lunch time")
    while True:
        schedule.run_pending
        time.sleep(1)
    
    
def SecondSchedule():
    print("Wrap up work")
    while True:
        schedule.run_pending
        time.sleep(1)
    
schedule.every().day.at("13:00").do(FirstSchedule)
schedule.every().day.at("18:00").do(SecondSchedule)

def main():
    FirstSchedule()
    SecondSchedule()

if __name__ == "__main__":
    main()        