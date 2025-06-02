#Write a program which contains one lambda function which accepts two parameters and return its multiplication
#Input : 4 3 OUTPUT : 12
#Input : 6 3 OUTPUT : 18


def MultiplyTwo(no1,no2):
    MultNumber = lambda no1,no2 : no1 * no2
    ret = MultNumber(no1,no2)
    print(ret)

def main():
    number1 = int(input("Enter first number : "))
    number2 = int(input("Enter Second number : "))
    MultiplyTwo(number1,number2)    

if __name__ == "__main__":
    main()    

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_10>python Assignment10_2.py
#Enter first number : 4
#Enter Second number : 3
#12

#C:\Users\Dhanashri\Desktop\Python\Assignment_10>python Assignment10_2.py
#Enter first number : 6
#Enter Second number : 3
#18