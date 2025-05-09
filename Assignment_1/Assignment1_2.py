#Write a program which contains one function named as ChkNum() which accept one parameter as number.If number is even then it should display 
# "Even number" otherwise display "Odd number" on console.

def ChkNum(number):
    if number % 2 == 0:
        print("Even number")
    else:    
        print("Odd number") 
   
no1 = int(input( "Enter the value :"))
(ChkNum(no1)) 

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_1>python Assignment1_2.py
#Enter the value :11
#Odd number

#C:\Users\Dhanashri\Desktop\Python\Assignment_1>python Assignment1_2.py
#Enter the value :8
#Even number