#Arithematic operation on two numbers.
#Write a program to accept two integers from user and display their
#Sum ,Difference ,product,division

def Sum(num1,num2):
    Result = num1+num2
    return Result

def Difference(num1,num2):
    Result = num1 - num2
    return Result

def Product(num1,num2):
    Result = num1 * num2
    return Result

def Division(num1,num2):
    Result = num1/num2
    return Result

def main():
    number1 = int(input("Enter First input : "))    
    number2 = int(input("Enter Second input: "))

    print("Sum : " ,Sum(number1,number2)) 
    print("Difference : " ,Difference(number1,number2)) 
    print("Product :" ,Product(number1,number2)) 
    print("Division : ",Division(number1,number2)) 

if __name__ =="__main__":
    main()

  #OUTPUT
  # C:\Users\Dhanashri\Desktop\Python\Assignment_5>python Assignment5_1.py
#Enter First input : 10
#Enter Second input: 2
#Sum :  12
#Difference :  8
#Product : 20
#Division :  5.0  



  