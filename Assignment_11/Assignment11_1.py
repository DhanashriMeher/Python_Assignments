#Print Numbers using Recursion
#write a recursive function to print numbers from 1 to N.

def RecNumber(n):
    if (n == 0):
        return 0
    else:
        RecNumber(n-1)
        print(n,end = " ")
     
def main():
    number = int(input("Enter the number : "))
    RecNumber(number)  

if __name__ == "__main__":
    main()

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_11>python Assignment11_1.py
#Enter the number : 5
#1 2 3 4 5    