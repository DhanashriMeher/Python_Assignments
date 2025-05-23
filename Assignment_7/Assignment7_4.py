#Accept list of number and use reduce () from functools to find the product of all numbers.
#Enter list : 2 3 4
#Product : 24

from functools import reduce
from operator import mul


def productList(num):
    return reduce(mul,num)

def main():
    Data = (input("Enter list : "))
    number_list = [int(num) for num in Data.split()]
    print("Product : ",productList(number_list))

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_7>python Assignment7_4.py
#Enter list : 2 3 4
#Product :  24
