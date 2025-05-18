#Write a program which accept one number from user and check whether
#number is prime or not
#Input : 5   OUTPUT: It is a prime number


def primeno(no):

    flag = False

    if no == 0 or no == 1:
        print("Please enter a valid number")
    elif no > 1:
         for i in range(2,no):
            if(no % i) == 0:
                flag = True
                break  

    if flag :
        print("It is not prime number")
    else:
        print("It is prime number")

def main():
    number = int(input("Enter the number : "))
    primeno(number)
    

if __name__ == "__main__":
    main()    

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_2>python Assignment2_5.py
#Enter the number : 5
#It is prime number

#C:\Users\Dhanashri\Desktop\Python\Assignment_2>python Assignment2_5.py
#Enter the number : 7
#It is prime number

#C:\Users\Dhanashri\Desktop\Python\Assignment_2>python Assignment2_5.py
#Enter the number : 6
#It is not prime number    