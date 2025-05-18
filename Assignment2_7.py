#write a program which accept one number and display below pattern
#Input 5
#OUTPUT :
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

def main():
    num = int(input("Enter the number : "))
    for i in range(1,num+1):
        for j in range(1,num+1):
            print( j , end = " ")
        print()     

if __name__ == "__main__" :
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_2>python Assignment2_7.py
#Enter the number : 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5