#Write a program which contains one lambda function which accepts one parameter and return power of two.
#Input : 4  OUTPUT : 16
#Input: 6   OUTPUT : 64

def PowerOfTwo(no1):
    PowerOfTwo = lambda no1:no1 ** 2   
    result = PowerOfTwo(no1)
    print(result)
def main():
    number = int(input("Enter number : "))
    PowerOfTwo(number)    

if __name__ == "__main__":
    main()    

#output
# C:\Users\Dhanashri\Desktop\Python\Assignment_4>python Assignment4_1.py
#Enter number : 4
#16

#C:\Users\Dhanashri\Desktop\Python\Assignment_4>python Assignment4_1.py
#Enter number : 6
#36    