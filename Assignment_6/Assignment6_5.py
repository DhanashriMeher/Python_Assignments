#Accept a number from the user and check whether it is prime or not.
 

def main():
    num = int(input("Enter a number: "))

    if num == 0 or num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                break
        else:
            print(num,"is a prime number")
       
    else:
        print(num,"is not a prime number")

    
if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_6>python Assignment6_5.py
#Enter a Number: 6
#6 is not a prime number

#C:\Users\Dhanashri\Desktop\Python\Assignment_6>python Assignment6_5.py
#Enter a Number: 7
#7 is a prime number
