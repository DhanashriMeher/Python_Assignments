#write a program which accept one number and display below pattern
#Input 5
#OUTPUT :
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

def main():
    num = int(input("Enter number :"))
    for i in range(num): 
        for j in range(1,i+2): 
            print(j , end= " ")
        print()        

if __name__ == "__main__":
    main()

#OUTPUT
#C:\Users\Dhanashri\Desktop\Python\Assignment_2>python Assignment2_8.py
#Enter number :5
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5
