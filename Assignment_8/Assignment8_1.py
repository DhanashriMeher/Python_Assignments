#Design python application which created two thread named as even and odd. 
# Even thread will display first 10 even numbers and 
# odd thread will display first 10 odd numbers.

import threading
def Evenno(no):
    print("Even numbers are : ")  

    for i in range(1,no):
        if(i % 2 == 0):
            print(i)

def Oddno(no):
    print("Odd numbers are : ")  

    for i in range(1,no):
        if(i % 2 != 0):
            print(i)


def main():

    T1 = threading.Thread(target= Evenno , args=(22,))
    T2 = threading.Thread(target = Oddno ,args =(20,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__=="__main__":
    main()    

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_8>python Assignment8_1.py
#Even numbers are :
#2
#4
#Odd numbers are :
#6
#1
#8
#3
#10
#5
#12
#7
#14
#9
#16
#11
#18
#13
#20
#15
#17
#19