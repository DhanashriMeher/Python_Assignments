#Write a script that simulates checking for email updates every 10
#seconds.(Use a print statement like "Checking mail..."
#instead of real email logic.)

import time

def checkEmail():
    print("Checking mail...")

print("Email checking started.")

def main():
    try:
        while True:
            checkEmail()
            time.sleep(10) 
    except KeyboardInterrupt:
        print("Email checker stopped.")

if __name__ =="__main__":
    main()        

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_17>python Assignment17_8.py
#Email checking started.
#Checking mail...
#Checking mail...
#Checking mail...
#Checking mail...
#Email checker stopped.