#Write a program which acccept N numbers from user and store it into list. Return addition of all prime numbers from that list.
#Main Python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named
#as MarvellousNum.Name of that function from main python file should be ListPrime().

#Input : Number of elements: 11
#Input Elements : 13 5 45 7 4 56 10 34 2 5 8
#Output:54

from marvellousNum import ChkPrime

def ListPrime(numbers):
    total = 0
    for num in numbers:
        if ChkPrime(num):
            total = total + num
    return total

def main():
    n = int(input("Number of elements: "))
    numbers = []

    print("Enter the elements:")
    for i in range(n):
        numbers.append(int(input()))

    result = ListPrime(numbers)
    print("Output:", result)

if __name__ =="__main__":
  main()

 #OUTPUT
 # C:\Users\Dhanashri\Desktop\Python\Assignment_3>Python Assignment3_5.py
#Number of elements: 11
#Enter the elements:
#13
#5
#45
#7
#4
#56
#10
#34
#2
#5
#8
Output: 32 