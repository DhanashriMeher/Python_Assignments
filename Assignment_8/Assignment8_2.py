#Design Python Application which creates two threads as evenfactor and oddfactor.Both the thread accept one parameter as integer.
#Evenfactor thread will display addition of even factors of given numbers 
#Oddfactor thread will display addition of odd factors of given numbers
#After execution of both the thread gets completed main thread should display message as "exit from main".

import threading

def Evenfactor(no):
    result = 0
    for i in range(1,no+1):
        if(no % i == 0 and i%2 == 0):
            print(i)
            result = result + i
    print("Addition of even factors : ",result)


def Oddfactor(no):
    result = 0
    for i in range(1,no+1):
        if(no % i == 0 and i%2 != 0):
            print(i)
            result = result + i
    print("Addition of odd factors : ",result)    

def main():
    Ret = int(input("Enter the EvenFactor and OddFactor Number : "))

    T1 = threading.Thread(target = Evenfactor ,args=(Ret , ))
    T2 = threading.Thread(target = Oddfactor ,args=(Ret, ))

    T1.start()
    T2.start()

    T1.join() 
    T2.join() 

    print("Exit from main")

if __name__=="__main__":
    main()    

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_8>python Assignment8_2.py
#Enter the EvenFactor and OddFactor Number : 10
#2
#10
#Addition of even factors :  12
#1
#5
#Addition of odd factors :  6
#Exit from main

   

        