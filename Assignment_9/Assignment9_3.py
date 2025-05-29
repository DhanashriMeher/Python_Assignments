#Create a python program that uses multiprocessing.Pool to compute factorial of numbers in a list.

import multiprocessing

def Fact(no):
    if (no == 0):
        return 1
    else:
       Fact1 = 1
       for i in range(1,no+1):
            Fact1 = Fact1 * i   
       return Fact1

def main():
    number = input("Enter the list of Factorial value : ")
    ret = [int(x) for x in number.split()]
    
    p = multiprocessing.Pool()
    result = p.map(Fact,ret)

    p.close()
    p.join()

    print("Factorial is : ",result)

if __name__ == "__main__"    :
    main()
    
    
#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_9>python Assignment9_3.py
#Enter the list of Factorial value : 4 5 2 3
#Factorial is :  [24, 120, 2, 6]    
