#Write a program which contains one lambda function which accepts two parameters and return its multiplication
#Input : 4 3 OUTPUT : 12
#Input : 6 3 OUTPUT : 18

def MultOfTwo(no1,no2):
    MultOfTwo = lambda no1,no2:no1 * no2   
    result = MultOfTwo(no1,no2)
    print(result)
def main():
    number1 = int(input("Enter first number : "))
    number2 = int(input("Enter Second number : "))
    MultOfTwo(number1,number2)    

if __name__ == "__main__":
    main()    


#Output
#C:\Users\Dhanashri\Desktop\Python\Assignment_4>python Assignment4_2.py
#Enter first number : 4
#Enter Second number : 3
#12

#:\Users\Dhanashri\Desktop\Python\Assignment_4>python Assignment4_2.py
#Enter first number : 6
#Enter Second number : 3
#18
