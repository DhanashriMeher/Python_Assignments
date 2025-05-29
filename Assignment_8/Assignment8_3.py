#Design python application which creates two threads as evenlist and oddlist.Both the threads accept list of integer as parameter
#Evenlist thread add all even elements from input list and display the addition.
#Oddlist thread add all odd elements from input list and display the addition


import threading

def Evenlist(nos):
    result = 0
    for i in nos:
        if(i % 2== 0):
            print("Even number from List : ",i)
            result =result+ i
    print("Evenlist addition is : ",result)

def Oddlist(nos):
    result = 0
    for i in nos:
        if(i % 2!=0):
            print("Odd number from list :",i)
            result = result + i
    print("Oddlist addition are : ",result)


def main():
    Data = input("Enter list of numbers : ")
    num_list = [int(no) for no in Data.split()]
    print("List : ",num_list)

    T1 =threading.Thread(target = Evenlist , args =(num_list,))
    T2 =threading.Thread(target = Oddlist , args =(num_list,))
   
    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()    
    


#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_8>python Assignment8_3.py
#Enter list of numbers : 7 8 9 4 5 6 1 2 3
#List :  [7, 8, 9, 4, 5, 6, 1, 2, 3]
#Even number from List :  8
#Even number from List :  4
#Odd number from list : 7
#Even number from List :  6
#Odd number from list : 9
#Odd number from list : 5
#Odd number from list : 1
#Odd number from list : 3
#Oddlist addition are :  25
#Even number from List :  2
#Evenlist addition is :  20