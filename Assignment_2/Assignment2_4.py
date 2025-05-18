#Write a program which accept one number from user and return addition of its factor.
#Input : 12   Output :16  (1+2+3+4+6)

def factor(no):
    if no <= 0:
        return 0

    Addition_of_no = 0 
    for i in range(1,no):
        if no % i == 0:
           Addition_of_no = Addition_of_no + i 
    return Addition_of_no     

def main():
    fact = int(input("Input : "))
    result = factor(fact)
    print(result)


if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_2>python Assignment2_4.py
#Input : 12
#16

#C:\Users\Dhanashri\Desktop\Python\Assignment_2>python Assignment2_4.py
#Input : 6
#6
    


