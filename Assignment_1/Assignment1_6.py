#Write a Program which accept number from user and check whether that number is positive or negative or zero.

number = int(input("Enter the value : "))
def Evenodd():
    if number > 0:
        print("Number is Positive")
    elif number < 0:
        print("Number is Negative")
    else :
        print("Number is Zero")        

if __name__ == "__main__":
    Evenodd()


#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_1>python Assignment1_6.py
#Enter the value : 11
#Number is Positive

#C:\Users\Dhanashri\Desktop\Python\Assignment_1>python Assignment1_6.py
#Enter the value : -8
#Number is Negative

#C:\Users\Dhanashri\Desktop\Python\Assignment_1>python Assignment1_6.py
#Enter the value : 0
#Number is Zero
