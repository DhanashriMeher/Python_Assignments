#Write a program which contains one lambda function which accepts one parameter and return power of two.
#Input : 4  OUTPUT : 16
#Input: 6   OUTPUT : 36

def PowerFun(no):
    PowerOfTwo = lambda no : no * no
    ret = PowerOfTwo(no)
    return ret

def main():
    number = int(input("Enter number : "))
    print(PowerFun(number))

if __name__ == "__main__":
    main()    

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_10>python Assignment10_1.py
#Enter number : 4
#16

#C:\Users\Dhanashri\Desktop\Python\Assignment_10>python Assignment10_1.py
#Enter number : 6
#36