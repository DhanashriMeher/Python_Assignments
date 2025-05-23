#Find Largest Among Three Numbers
#Accept three numbers from the user and print the largest using nested if-else
#statement.

def LargestNo(no1,no2,no3):
    if (no1 >= no2) and (no1 >= no3):
        print("Largest number is : ", no1)
    
    elif(no2 >= no1) and (no2 >= no3):
        print("Largest number is :", no2)
    else:
        print("Largest number is : ", no3)


def main():
    print("Enter three numbers: ")
    number1 = float(input())
    number2 = float(input())
    number3 = float(input())

    LargestNo(number1,number2,number3)

if __name__ == "__main__" :
    main()

 #OUTPUT
 # C:\Users\Dhanashri\Desktop\Python\Assignment_5>python Assignment5_4.py
#Enter three numbers:
#5
#9
#3
#Largest number is : 9.0   