#Accept a number and print its factorial using a for loop.

def main():
    fact = 1
    n = int(input("Enter the number : "))
    for i in range(1,n+1):  
        fact = fact * i
    print(fact)    


if __name__ == "__main__":
    main()    

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_6>python Assignment6_4.py
#Enter the number : 5
#120