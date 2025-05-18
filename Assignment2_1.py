# Create on module named as Arithmetic which contains 4 functions as Add() for addition,Sub() for substraction,Mult() for multiplication
#and Div() for division.All functions accepts two parameters as number and perform the operation.Write a python program which call all the 
#functions from Arithematic module by accepting the paramaters from user.
import Arithemetic

def main():
    print("Enter first number :")
    no1 =int(input())

    print("Enter second number :")
    no2 =int(input())

    ans = Arithemetic.Add(no1,no2)
    print("Addition of two numbers are : " ,ans)

    Substraction = Arithemetic.Sub(no1,no2)
    print("Substraction of two numbers are : " ,Substraction)

    Multiplication = Arithemetic.Mult(no1,no2)
    print("Multiplication of two numbers are : " ,Multiplication)

    Division = float(Arithemetic.Div(no1,no2))
    print("Division of two numbers are : " ,Division)


if __name__ == "__main__":
    main()