#Create task that runs once every day at 9.00 AM and prints "Namaskar..."

import schedule
import time

def MySchedule():
    print("Namaskar.....!!!")

def main():
    schedule.every().day.at("09.00").do(MySchedule)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
