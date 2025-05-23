#Accept a number from the user and print its multiplication table upto 10

def multTable(num):
    for i in range(1,11):
        print(num ,'X', i ,'=' , num*i) 

def main():
    num = int(input("Enter a number :"))
    multTable(num)

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_6>python Assignment6_3.py
#Enter a number :7
#7 X 1 = 7
#7 X 2 = 14
#7 X 3 = 21
#7 X 4 = 28
#7 X 5 = 35
#7 X 6 = 42
#7 X 7 = 49
#7 X 8 = 56
#7 X 9 = 63
#7 X 10 = 70