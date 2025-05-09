#Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers
# Input 11 5     Output : 16

def Add():
    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))
    numbers = no1 + no2
    print("Addition of two numbers : ",numbers)

if __name__ == "__main__":
    Add()    


#output
#C:\Users\Dhanashri\Desktop\Python\Assignment_1>python Assignment1_3.py
#Enter first number : 11
#Enter second number : 5
#Addition of two numbers :  16