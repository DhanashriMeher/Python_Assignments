#Design python application which contans two threads named as thread1 and thread2.Thread1 display 1 to 50 
#and thread2 display 50 to 1 in a reverse order on screen.After execution of thread1 gets completed then schedule thread2.

import threading
import time

def ShowNumbers(num):
    for i in range(1,num+1):
        print (i, end = " ")

def ReverseNumbers(num):
    for i in range(num,0,-1):
        print(i,end = " ")        

def main():
    print("1 to 50 numbers are :")
    T1 = threading.Thread(target = ShowNumbers ,args=(50,))
    T1.start()
    T1.join()

    start_time = time.time()
    print("\n50 to 1 numbers are :" ,)
    T2 = threading.Thread(target = ReverseNumbers ,args=(50,))
    T2.start()
    T2.join()

    end_time= time.time()

    print("\nTime required for execution is : " ,end_time-start_time)


if __name__ == "__main__":
    main()

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_8>python Assignment8_5.py
#1 to 50 numbers are :
#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50
#50 to 1 numbers are :
#50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
#Time required for execution is :  0.0010609626770019531    
