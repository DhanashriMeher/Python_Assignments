#Write a program which accept one number from user and write its factorial

def main():
    fact = 1
    n = int(input("Enter the number : "))
    for i in range(1,n+1):  
        fact = fact * i
    print(fact)    


if __name__ == "__main__":
    main()    

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_2>python Assignment2_3.py
#Enter the number : 5
#120
