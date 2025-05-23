#Print Sum of Even numbers between 1 and 100. Use a loop to find and print the sum of
#all even numbers from 1 to 100.

def SumOfEven():
    sum = 0
    for i in range(1,101):
        if(i % 2 == 0):
            sum = sum+i
    return sum

def main():
    print("Sum of Even numbers between 1 to 100 is : ",SumOfEven())

if __name__ =="__main__":
    main()

#OUTPUT
# C:\Users\Dhanashri\Desktop\Python\Assignment_6>python Assignment6_2.py
#Sum of Even numbers between 1 to 100 is :  2550    


