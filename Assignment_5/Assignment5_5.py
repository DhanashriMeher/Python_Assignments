#Even or Odd Number Check
#Write a program to check whether the entered number is even or odd.

def EvenOdd(num):
    if (num % 2 == 0):
        print(num ," is an Even number")
    else:
        print(num  ," is an Odd number")

def main():
    Result = int(input("Enter number : "))
    EvenOdd(Result)

if __name__ == "__main__" :
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_5>python Assignment5_5.py
#Enter number : 17
#17  is an Odd number

#C:\Users\Dhanashri\Desktop\Python\Assignment_5>python Assignment5_5.py
#Enter number : 6
#6  is an Even number
           