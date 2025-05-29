#Design python application which creates three threads as small,capital,digits.All threads accepts string as parameter.
#Small thread display number of small characters,capital thread display number of capital characters and digit thread display number of digit.
#Display id and name each thread.

import threading

def CountSmallChar(str1):
    print("Id of thread1 : ",threading.get_ident())
    print("Name of Thread : " ,threading.current_thread().name)

    count = 0
    for i in str1:
        if(i.islower()):
            count = count + 1
    print("Count of Small of characters : ",count)
    


def CountCapitalChar(str2):
    print("Id of thread2 : ",threading.get_ident())
    print("Name of Thread2 : ",threading.current_thread().name)

    count = 0
    for i in str2:
        if(i.isupper()):
            count = count + 1
    print("Count of Capital of characters : ",count)
   

def CountDigits(str3):
    print("Id of thread3 : ",threading.get_ident())
    print("Name of Thread3 : ",threading.current_thread().name)

    count = 0
    for i in str3:
        if(i.isdigit()):
            count = count + 1
    print("Count of digits : ",count)


def main():
    Result = input("Enter String : ")

    T1 = threading.Thread(target = CountSmallChar , args = (Result , ))
    T2= threading.Thread(target = CountCapitalChar , args = (Result , ))
    T3 = threading.Thread(target = CountDigits , args = (Result , ))
    
    T1.start()
    T2.start()
    T3.start()
  
    T1.join()
    T2.join()
    T3.join()

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_8>python Assignment8_4.py
#Enter String : HelloWorld90
#Id of thread1 :  15624
#Name of Thread :  Thread-1 (CountSmallChar)
#Id of thread2 :  15636
#Count of Small of characters :  8
#Name of Thread2 :  Thread-2 (CountCapitalChar)
#Id of thread3 :  1960
#Count of Capital of characters :  2
#Name of Thread3 :  Thread-3 (CountDigits)
#Count of digits :  2