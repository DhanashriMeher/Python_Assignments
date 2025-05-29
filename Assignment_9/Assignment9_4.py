#Create a python program that compare execution time of summing numbers from 1 to 10 million using normal function,threading and 
#multiprocessing

import time
import multiprocessing
import threading

def NormalFun():
    Result = 0
    for i in range(1,10000001):
        Result = Result + i
    return Result
            

def main():
    print("Addition from 1 to 10 million numbers are : ",NormalFun())

    start_time = time.time()
    NormalFun()
    end_time = time.time()
    print(f"Execution time for normal function : {end_time - start_time :.4f} seconds")

    start_time1 = time.time()
    T1 = threading.Thread(target = NormalFun)
    T1.start()
    T1.join()
    End_time1 = time.time()
    print(f"Execution time for Thread function : {start_time1-End_time1: .4f} seconds")
    
    start_time2 = time.time()
    p =multiprocessing.Process(target= NormalFun)
    p.start()
    p.join()
    End_time2 = time.time()
    print(f"Execution time for Multiprocessing function : {start_time2-End_time2:.4f} seconds")


if __name__ == "__main__":
    main()    

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_9>python Assignment9_4.py
#Addition from 1 to 10 million numbers are :  50000005000000
#Execution time for normal function : 1.3509 seconds
#Execution time for Thread function : -1.1975 seconds
#Execution time for Multiprocessing function : -1.4310 seconds
    
