#Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise returns false.

def division(num):
    return  num % 5 == 0
     
number = int(input("Enter the value : "))
if division(number):
    print("True")
else:
   print("False")    


#OR

number = int(input("Enter the value : "))
def division(num):
    if num % 5 == 0:
        print("True")
    else:
        print("False")    

if __name__ == "__main__":
    division(number)

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_1>python Assignment1_7.py
#Enter the value : 25
#True

#C:\Users\Dhanashri\Desktop\Python\Assignment_1>python Assignment1_7.py
#Enter the value : 8
#False





