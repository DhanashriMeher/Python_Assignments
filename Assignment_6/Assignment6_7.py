#Accept 5 numbers from the user.Find and print the largest number.

def LargestNo(num1,num2,num3,num4,num5):
    if((num1 >= num2) and (num1 >= num3) and (num1 >= num4) and (num1 >= num5)):
        print("Maximum number is : ", num1)

    elif((num2 >= num1) and (num2 >= num3) and (num2 >= num4) and (num2 >= num5)):
        print("Maximum number is : ", num2)

    elif((num3 >= num1) and (num3 >= num2) and (num3 >= num4) and (num3 >= num5)):
        print("Maximum number is : ", num3)

    elif((num4 >= num1) and (num4 >= num2) and (num4 >= num3) and (num3 >= num5)):
        print("Maximum number is : ", num4)
    else:
         print("Maximum number is : ", num5)
    
def main():
    print("Enter 5 numbers : ")

    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    num5 = float(input())

    LargestNo(num1,num2,num3,num4,num5)

if __name__ == "__main__":
    main()    

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_6>python Assignment6_7.py
#Enter 5 numbers :
#23
#89
#12
#56
#45
#Maximum number is :  89.0

 