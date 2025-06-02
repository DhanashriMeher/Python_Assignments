#Write a program which contains filter(),map( ) and reduce() in it.Python application which contains one list of numbers.
#List contains the numbers which are accepted from user. 
#Filter should filter out all prime numbers.Map function will multiply each number by 2.  
#Reduce will return maximum number from that numbers.(You can also use normal functions instead of lambda functions)

from functools import reduce

def PrimeNo(num):
   if (num < 2):
    return False
   else :
    for i in range(2,num):
        if (num % i == 0):
            return False
    return True
           

def multiply_by_two(n):
    return n * 2

def find_max(x, y):
    if x > y:
        return x
    else:
        return y


def main():
    Data = input("Enter numbers : ")
    number_list = [int(num) for num in Data.split()]
    print("Input data : ",number_list)

    FData = list(filter(PrimeNo,number_list))
    print("List after filter : ",FData)

    MData = list(map(multiply_by_two,FData))
    print("Map Data : ",MData)

    RData = reduce(find_max,MData)
    print("Reduce Data : ",RData)

if __name__ == "__main__":
     main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_10>python Assignment10_5.py
#Enter numbers : 2 70 11 10 17 23 31 77
#Input data :  [2, 70, 11, 10, 17, 23, 31, 77]
#List after filter :  [2, 11, 17, 23, 31]
#Map Data :  [4, 22, 34, 46, 62]
#Reduce Data :  62