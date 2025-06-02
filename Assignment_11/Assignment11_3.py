#Write a Recursive function to calculate the sum of digits of a number.

Sum = 0

def SumOfDigit(no):
    global Sum
    if(no >= 1):
        Sum = Sum + no
        no = no - 1
        SumOfDigit(no)
    return Sum        

def main():
    ret = SumOfDigit(4)
    print(ret)

if __name__ == "__main__":
    main()    

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_11>python Assignment11_3.py
#10      