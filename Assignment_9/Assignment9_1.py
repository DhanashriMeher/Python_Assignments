#Create a python program that starts 3 threads, each printing numbers from 1 to 5 with a delay of 1 second. Use threading.Thread.

import threading
import time

def CountNo(no):
    for i in range(1,no+1):
        print("Thread1 : " ,i)
        time.sleep(1)
       
def CountNo1(no):
    for i in range(1,no+1):
        print("Thread2 : " ,i)
        time.sleep(1)


def CountNo2(no):
    for i in range(1,no+1):
        print("Thread3 : " ,i)
        time.sleep(1)


def main():
    T1 = threading.Thread(target=CountNo , args = (5,))
    T2 = threading.Thread(target=CountNo1 , args = (5,))
    T3 = threading.Thread(target=CountNo2 , args = (5,))   

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()         
           
if __name__ == "__main__":
    main()   


#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_9>python Assignment9_1.py
#Thread1 :  1
#Thread2 :  1
#Thread3 :  1
#Thread1 :  2
#Thread2 :  2
#Thread3 :  2
#Thread1 :  3
#Thread2 :  3
#Thread3 :  3
#Thread1 :  4
#Thread2 :  4
#Thread3 :  4
#Thread1 :  5
#Thread2 :  5
#Thread3 :  5